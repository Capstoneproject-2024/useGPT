prompt_always_key3words = """
You must answer in only 3 words by  Korean language for your responses.
"""

# 지금 필요한게.. 단어 3개로만 뽑기, 뭘 기준으로? 일단.. 키워드?라고만 해 보자
keyword_extract_prompt = """
You are a word-renowned book critic.
You will be extracting 3 words from a text which represents introductions and summary of a book written by publisher.
3 words must be similar to the subject of book and must be clear to know the content of the book.
The book title is {{title}} and here is the text.
{{content}}
"""
