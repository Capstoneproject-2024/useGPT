from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

from textEX import textList
from const import *
from utils import inject_variables

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"


client = AsyncOpenAI(api_key=GPT_API_KEY)


async def extract(client):
    for i in range(len(textList)):
        prompt = inject_variables(publisher_keyword_extract_prompt, textList[i])
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": prompt + prompt_always_keywords},
            ],
            temperature=1.3,
            top_p=0.8,
            frequency_penalty=0,
            presence_penalty=1,
        )

        # print(response)
        temp = response.model_dump()
        print(temp["choices"][0]["message"]["content"] + "\n")


async def main():
    await extract(client=client)


# main 함수 실행
asyncio.run(main())
