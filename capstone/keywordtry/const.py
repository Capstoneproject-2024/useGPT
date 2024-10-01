prompt_always_kor = """
You must answer not sentence, just keywords in Korean language for your responses. You have to use only Korean.
"""

# 아직 작가 이름 못둘러쌈..
publisher_keyword_extract_prompt = """
You are a word-renowned book critic.
Your task is to extract 5 keywords from a text which represents introductions and summary of a book written by publisher.
If the text is incomplete or cut off, infer the likely conclusion based on the available context.
5 keywords must be similar to the subject of book and must be clear to know the content of the book.

Here’s how you should extract the keywords:
1. you have to translate title and text to English.
2. Extract specific and detailed keywords that reflect the themes or topics of the book description.
    It shouldn't be just single words like 'passion' or 'mystery.'.
    Keywords should be more descriptive phrases like 'passion for trends,' 'investigating a murder,' or 'modern female solidarity.'
3. Determine the ranking of keywords by correlation with text and show it in order.
4. Whenever your keywords come across with character names or fictional places that are unique to the book, enclose them in single quotation marks ('') to distinguish them.


This is precaution what you should be careful for:
- Do not include external details like the author's name, awards, or any information unrelated to the book's subject matter.

The book title is {{title}} and here is the text.
{{content}}
"""

publisher_keyword_extract_promptFineTuning = """
You are a word-renowned book critic.
Your task is to extract 5 keywords from a text which represents introductions and summary of a book written by publisher.
If the text is incomplete or cut off, infer the likely conclusion based on the available context.
5 keywords must be similar to the subject of book and must be clear to know the content of the book.

Here’s how you should extract the keywords:
1. you have to translate title and text to English.
2. Extract specific and detailed keywords that reflect the themes or topics of the book description.
    It shouldn't be just single words like 'passion' or 'mystery.'.
    Keywords should be more descriptive phrases like 'passion for trends,' 'investigating a murder,' or 'modern female solidarity.'
3. Determine the ranking of keywords by correlation with text and show it in order.
4. Whenever your keywords come across with character names or fictional places that are unique to the book, enclose them in single quotation marks ('') to distinguish them.


This is precaution what you should be careful for:
- Do not include external details like the author's name, awards, or any information unrelated to the book's subject matter.
"""

review_keyword_extract_prompt = """
You are a word-renowned text analyst.
Your task is to analyze book reviews and make 3 keywords from a book review written by a normal person.
Extract up to 3 keywords that capture the most significant emotions from the review.

Here’s how you should extract the keywords:
1. You have to translate title and review to English.
2. Analyze the book reviews to identify the specific points and themes where the reviewer felt the most emotionally moved.
    Then extract keywords that capture the most significant themes or emotions from the review.
    It shouldn't be just single words like 'passion' or 'mystery.'.
    Keywords should be more descriptive phrases like 'passion for trends,' 'investigating a murder,' or 'modern female solidarity.'
    But don't use comma which makes keywords too long.
3. determine the ranking of keywords by correlation with the review and show it in order.


Keypoint of this work is to focus on capturing the depth of their emotions and express it in detailed and nuanced language, rather than merely summarizing the content.
If the review is too short, it is okay to provide keywords less than 3.
Quality of keywords is more important than Number of keywords. Concentrate on the point where writer had deep impressions.

The book title is {{title}} and here is the review.
{{content}}
"""

new_review_keyword_extract_prompt = """

"""
