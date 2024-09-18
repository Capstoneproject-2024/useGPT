from openai import OpenAI
from dotenv import load_dotenv
import os
from textEX import textList
from const import *

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")

client = OpenAI(api_key=GPT_API_KEY)


async def extract(client):
    for i in range(1):
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": prompt_always_key3words
                    + keyword_extract_prompt
                    + textList[i],
                },
            ],
            # temperature=0.75,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0.75,
        )

        print(response)
        return response


extract(client=client)
