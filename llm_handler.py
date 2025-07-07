import requests
import json
from langchain.prompts import PromptTemplate

def call_llm(user_input, config):
    # Step 1: Create PromptTemplate
    prompt = PromptTemplate(
        input_variables=["thought"],
        template="""
You are a self-reflection assistant.
Analyze the user's thought and give back a 3-part reflection:

1. Emotional Interpretation
2. Rational Perspective
3. Growth-Oriented Suggestion

User's Thought: {thought}
"""
    )

    # Step 2: Format input
    final_prompt = prompt.format(thought=user_input)

    # Step 3: Send to OpenRouter API
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {config['openrouter_api_key']}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {"role": "user", "content": final_prompt}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception(f"LLM API Error: {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
