from openai import OpenAI
import os
import tiktoken
from makeDataSet import forJsonl

GPT_API_KEY = os.environ.get("GPT_API_KEY")
OPENAI_MODEL = "gpt-4o-mini-2024-07-18"

client = OpenAI(api_key=GPT_API_KEY)

# 파일 업로드
# client.files.create(file=open("../../learnData.jsonl", "rb"), purpose="fine-tune")

# # 미세조정 모델 만들기
# client.fine_tuning.jobs.create(
#     training_file="file-KDuklvFcJueCbT485VgzHMQp", model=OPENAI_MODEL
# )


# 토큰 개수 확인 - 비용..
encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model(OPENAI_MODEL)
encoding.encode("tiktoken is great!")


# 가격 추정할만한 사이트 FAQ https://help.openai.com/en/articles/7127982-can-i-fine-tune-gpt-4o-or-gpt-4

# 여기에 epoch 곱해야 최종 토큰 수임 (현재 epoch = 3)
token = 0
for i in range(len(forJsonl)):
    token += len(
        encoding.encode(
            forJsonl[i]["messages"][0]["content"]
            + forJsonl[i]["messages"][1]["content"]
            + forJsonl[i]["messages"][2]["content"]
        )
    )

print("toekn count : ", token)
