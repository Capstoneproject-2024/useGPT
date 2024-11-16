import os
from fastapi import FastAPI, Query
from dotenv import load_dotenv
from openai import AsyncOpenAI

from makeQustion import makeQuestion

app = FastAPI()

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini-2024-07-18"


client = AsyncOpenAI(api_key=GPT_API_KEY)

"""
양식
{
    "questions": [
        "Question 1 will be here in String type",
        "Question 2 will be here in String type",
        "Question 3 will be here in String type",
        "Question 4 will be here in String type",
        "Question 5 will be here in String type",
    ]
}
"""


@app.get("/quote_question")
async def getQuestion(
    keyword: str = Query(..., description="책 키워드"),
    groupWord: str = Query(..., description="그룹 단어"),
):

    textList = [
        {"text": keyword, "keyword": groupWord}  # text = 책 키워드, keyword = 그룹 단어
    ]

    return {"questions": await makeQuestion(client=client, keywordList=textList)}
