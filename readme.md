<p><img src="./imgs/readme_main.webp"></p>

# SearchBasedRAG

This repository hosts a cutting-edge Retrieval-Augmented Generation (RAG) coding agent that integrates advanced tools to streamline coding workflows. It combines state-of-the-art search and generation capabilities with:

- **Morphic**: Generative search engine for intuitive data retrieval.  
- **Ollama**: Local LLM inference for secure and privacy-preserving AI.  
- **Open WebUI**: A self-hosted platform for seamless user interaction.  
- **Faiss**: High-performance vector similarity search for document retrieval.  
- **BAAI/bge-large-en-v1.5**: State-of-the-art embedding model optimized for dense retrieval tasks.  
- **Nginx**: Reverse proxy server for routing and scalability.  

## Features

- 🔍 **Search-Based RAG Pipeline**: Efficient retrieval of relevant information using Faiss and Morphic.  
- 🤖 **LLM Integration**: Local inference with Ollama for generating context-aware responses.  
- 🌐 **Web UI**: User-friendly interface powered by Open WebUI.  
- 🚀 **Scalability**: Handles large datasets with GPU acceleration via Faiss and BAAI embeddings.  
- 🔧 **Reverse Proxy Setup**: Nginx integration for routing and API endpoint customization.

## Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  

## About the Project

**SearchBasedRAG** is designed to enhance developer productivity through intelligent search and code generation. By integrating fast vector retrieval (via Faiss) with rich language understanding (via Ollama and BAAI embeddings), the system enables rapid and relevant access to technical documentation, code samples, and online resources—all in a unified conversational workflow.

The architecture combines local and web-based knowledge retrieval to ensure both contextual relevance and up-to-date information sourcing. This hybrid approach makes it suitable for both secure enterprise environments and open-source development.

## Installation

*(To be completed)*

## Usage

To use the pipeline, simply call the `pipeline(user_query)` function with a natural language query:

```python
response, local_context, web_results = pipeline("How do I deploy a model with KServe?")
```

The system will:
1. Rephrase the query for optimal embedding and search.
2. Retrieve relevant documentation chunks using Faiss.
3. Fetch additional results from the web via Tavily.
4. Generate a context-rich, final response using an LLM hosted locally via Ollama.

### Components:
- **`faiss_search(query)`**: Retrieves relevant passages from local docs.
- **`query_llama_rag(user_query, system_prompt, rag_context)`**: Interacts with LLM to generate responses.
- **`pipeline(user_query)`**: Orchestrates local and web search with RAG-style inference.

## Technologies Used

- **Python**: Primary language for implementation.
- **Pandas / NumPy**: Data handling and numerical operations.
- **Faiss**: Vector similarity search for fast retrieval.
- **FlagEmbedding**: Embedding model from BAAI with instruction tuning.
- **Ollama**: Local LLM inference framework.
- **Tavily API**: Web search integration.
- **Langchain**: Text chunking and splitting for optimal context.
- **JSON / OpenAI Format**: For context-rich input/output handling.
- **Nginx**: Optional reverse proxy for deployment.

## Contributing

Contributions are welcome! If you'd like to:
- Fix bugs
- Suggest improvements
- Add new features
- Improve documentation

Feel free to open a pull request or submit an issue. Please ensure your changes follow the existing style and include relevant test coverage where necessary.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

> Still under development — stay tuned for more features and integrations 🚧

Let me know if you’d like the README formatted in Markdown or saved to a file.
