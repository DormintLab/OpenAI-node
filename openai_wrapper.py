import openai
from pydantic import BaseModel
from utils import get_http_client


pricing = {
    "gpt-3.5-turbo-4k": {
        "prompt": 0.0015,
        "completion": 0.002,
    },
    "gpt-3.5-turbo-16k": {
        "prompt": 0.003,
        "completion": 0.004,
    },
    "gpt-4-8k": {
        "prompt": 0.03,
        "completion": 0.06,
    },
    "gpt-4-32k": {
        "prompt": 0.06,
        "completion": 0.12,
    },
    "gpt-4o-mini": {
        "prompt": 0.0015,
        "completion": 0.006,
    },
    "text-embedding-ada-002-v2": {
        "prompt": 0.0001,
        "completion": 0.0001,
    },
}


def get_async_openai_client(OPENAI_API_KEY):
    client = openai.AsyncClient(
        api_key=OPENAI_API_KEY,
        http_client=get_http_client(),
    )
    return client


async def get_async_openai_text_api(client, prompt, text):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )
    return response.choices[0].message.content


async def get_async_openai_text_embedding(client, texts):
    embedding_model = "text-embedding-3-small"
    result = await client.embeddings.create(input=texts, model=embedding_model)
    return result.data
