import numpy as np
import pandas as pd
import json

import faiss
import ollama
from FlagEmbedding import FlagModel
from langchain.text_splitter import RecursiveCharacterTextSplitter

from system_prompts.coder_agent import system_prompt as coder_system_prompt
from system_prompts.retrieve_agent import system_prompt as retrieve_system_prompt
from agents.tvily_searcher import search as tvily_search


instr = "Represent this sentence for searching relevant passages: Provide a detailed and accurate representation of the query to retrieve relevant technical documentation, explanations, or examples related to KServe."

MODEL = FlagModel('BAAI/bge-large-en-v1.5', 
                  query_instruction_for_retrieval=instr,
                  use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performance degradation

CHUNKS = pd.read_json("./data/kserve/kserve_rag_data.json")
metadata = pd.json_normalize(CHUNKS["metadata"])
CHUNKS = CHUNKS.drop("metadata", axis=1).join(metadata)
metadata = None

# FAISS_RES = faiss.StandardGpuResources()
INDEX: faiss.Index = faiss.read_index("faiss/faiss_index_mmap.index", faiss.IO_FLAG_MMAP)
# GPU_INDEX: faiss.Index = faiss.index_cpu_to_gpu(FAISS_RES, 0, INDEX)

def faiss_search(query, k=5):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    query_chucks = text_splitter.split_text(query)

    q_embeddings = MODEL.encode_queries(query_chucks)
    q_embeddings = np.array(q_embeddings, dtype=np.float32)

    distances, indices = INDEX.search(q_embeddings, k)
    retrieved_chunks = [CHUNKS["content"][i] for i in indices[0]]
    context = "\n".join([f"- {chunk}" for chunk in retrieved_chunks])

    return context


def query_llama_rag(user_query, system_prompt, rag_context=""):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Query: {user_query}\nContext: {rag_context}"}
    ]

    response = ollama.chat(model="llama3.3:70b", messages=messages)

    return response["message"]["content"]

def pipeline(user_query:str):
    # local database search
    retrieve_response = query_llama_rag(user_query, retrieve_system_prompt)
    rag_context = faiss_search(retrieve_response)

    # web search
    web_response = tvily_search(user_query)
    web_results = web_response["results"]
    web_res_json = json.dumps(web_results, indent=4)

    rag_context_web = rag_context
    rag_context_web += f"""
    \n\nWeb Results:\n
    ```json
    {web_res_json}
    ```
    """

    final_response = query_llama_rag(user_query, coder_system_prompt, rag_context_web)

    return final_response, rag_context, web_results