from openai import OpenAI
import json


def gpt_chat_completion(prompt: str, system_prompt:str):
    client = OpenAI()
    
    # tools = [{
    #     "type": "function",
    #     "function": {
    #         "name": "control_lights",
    #         "description": "Control the IoT LED lights based on the user's instructions. If the prompt requires multiple LED controls, provide them all in the list returned.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "codes": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "string",
    #                         "enum": ["A1", "A0", "B1", "B0"]
    #                     }
    #                 }
    #             },
    #             "required": ["codes"],
    #             "additionalProperties": False
    #         },
    #         "strict": True
    #     }
    # }]

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        # tools=tools
    )
    return completion.choices[0].message.content

    # tool_calls = completion.choices[0].message.tool_calls[0]

    # codes_json = tool_calls.function.arguments

    # codes = json.loads(codes_json)

    # with open("data.json", "w", encoding="utf-8") as f:
    #     json.dump(codes, f, ensure_ascii=False, indent=4)

    # return codes
