import csv
import json

from const import *
from utils import *
from extract import *

load_dotenv()

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini-2024-07-18"
FINETUNEING_MODEL = os.environ.get("FINETUNING_MODEL")


client = AsyncOpenAI(api_key=GPT_API_KEY)


# 데이터 형식 - 제목, 책소개글, (수제작) 키워드
def makeLearningSet():
    f = open("c:/Dev/keywordextract/testBookInfo.csv", mode="r", encoding="utf-8")
    rdr = csv.reader(f)

    count = 0
    bookInfoL = []
    answerL = []
    for line in rdr:
        count += 1
        bookInfoL.append(
            {
                "title": line[0],
                "content": line[1],
            }
        )
        answerL.append(line[2])
        if count == 10:
            break

    forJsonl = []
    for i in range(10):
        forJsonl.append(
            {
                "messages": [
                    {
                        "role": "system",
                        "content": publisher_keyword_extract_promptFineTuning
                        + prompt_always_kor,
                    },
                    {
                        "role": "user",
                        "content": "The book title is \n"
                        + bookInfoL[i]["title"]
                        + "\n"
                        + "and here is the text.\n"
                        + bookInfoL[i]["content"],
                    },
                    {
                        "role": "assistant",
                        "content": answerL[i],
                    },
                ]
            }
        )

    # jsonl 파일로 저장
    with open("../../validationData.jsonl", "w", encoding="utf-8") as f:
        for entry in forJsonl:
            json_str = json.dumps(
                entry, ensure_ascii=False
            )  # ensure_ascii=False로 한글을 깨지지 않게
            f.write(json_str + "\n")


async def makeGenreDB():
    f = open("c:/Dev/keywordextract/bookDescriptions.csv", mode="r", encoding="utf-8")
    rdr = csv.reader(f)

    # count = 0
    bookInfoL = []

    for line in rdr:
        bookInfoL.append({"title": line[0], "content": line[2]})
        # count += 1
        # if count == 3:
        #     break

    result = await extractGenre(client=client, textList=bookInfoL)

    with open(
        "c:/Dev/keywordextract/genreExtract.csv",
        mode="w",
        newline="",
        encoding="utf-8",
    ) as file:
        # csv.writer 객체 생성
        writer = csv.writer(file)

        # 데이터를 한 줄씩 작성
        for g in result:
            writer.writerow(g)


async def makeBookKeywordDB():
    f = open("c:/Dev/keywordextract/bookDescriptions.csv", mode="r", encoding="utf-8")
    rdr = csv.reader(f)

    # count = 0
    bookInfoL = []

    for line in rdr:
        bookInfoL.append({"title": line[0], "content": line[2]})
        # count += 1
        # if count == 10:
        #     break

    result = await extractPublisher(
        client=client, textList=bookInfoL, model=OPENAI_MODEL
    )

    with open(
        "c:/Dev/keywordextract/bookKeywordExtract.csv",
        mode="w",
        newline="",
        encoding="utf-8",
    ) as file:
        # csv.writer 객체 생성
        writer = csv.writer(file)

        # 데이터를 한 줄씩 작성
        for g in result:
            writer.writerow(g)


async def main():
    # await makeGenreDB()
    await makeBookKeywordDB()


# main 함수 실행
asyncio.run(main())
