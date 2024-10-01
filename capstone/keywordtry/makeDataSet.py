import csv
import json

from const import *
from utils import *

f = open("../../bookInfo.csv", mode="r", encoding="utf-8")
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
    if count == 50:
        break


forJsonl = []
for i in range(50):
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
with open("../../learnData.jsonl", "w", encoding="utf-8") as f:
    for entry in forJsonl:
        json_str = json.dumps(
            entry, ensure_ascii=False
        )  # ensure_ascii=False로 한글을 깨지지 않게
        f.write(json_str + "\n")
