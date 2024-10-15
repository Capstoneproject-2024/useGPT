from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

from const import *
from testEX import *
from utils import *

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini-2024-07-18"


client = AsyncOpenAI(api_key=GPT_API_KEY)


async def makeQuestion(clinet, keywordList):
    questions = []
    for i in range(len(keywordList)):
        prompt = inject_variables(SecondLevel_Question_prompt, keywordList[i])
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": prompt + prompt_always_kor},
            ],
            temperature=1,
            top_p=0.75,
            frequency_penalty=0.5,
            presence_penalty=1,
        )

        # print(response)
        temp = response.model_dump()
        questions.append(temp)
        print(
            "text : "
            + keywordList[i]["text"]
            + " keyword :"
            + keywordList[i]["keyword"]
        )
        print(temp["choices"][0]["message"]["content"] + "\n")
    return questions


async def main():
    await makeQuestion(clinet=client, keywordList=sample1)


# main 함수 실행
asyncio.run(main())
