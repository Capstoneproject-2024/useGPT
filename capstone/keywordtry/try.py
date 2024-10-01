from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

from textEX import *
from const import *
from utils import inject_variables
from reviewEX import *

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini-2024-07-18"


client = AsyncOpenAI(api_key=GPT_API_KEY)


# 출판사 키워드 추출 with 기본 모델
async def extractPublisher(client, textList, model):
    for i in range(len(textList)):
        prompt = inject_variables(publisher_keyword_extract_prompt, textList[i])
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": prompt + prompt_always_kor},
            ],
            temperature=1.3,
            top_p=0.8,
            frequency_penalty=0,
            presence_penalty=1,
        )

        # print(response)
        temp = response.model_dump()
        print(temp["choices"][0]["message"]["content"] + "\n")


# 리뷰 키워드 추출
async def extractReview(client):
    for i in range(len(goodReviewList)):
        prompt = inject_variables(review_keyword_extract_prompt, goodReviewList[i])
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": prompt + prompt_always_kor},
            ],
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1,
        )

        # print(response)
        temp = response.model_dump()
        print(str(i) + "\n" + temp["choices"][0]["message"]["content"] + "\n")


async def main():
    # await extractPublisher(client=client, textList=testSet, model=OPENAI_MODEL)
    await extractPublisher(
        client=client,
        textList=testSet,
        model="ft:gpt-4o-mini-2024-07-18:personal::ADV4GCef",
    )
    # await extractReview(client=client)


# main 함수 실행
asyncio.run(main())
