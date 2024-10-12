prompt_always_kor = """
You must answer in Korean language for your responses. You have to use only Korean.
"""

SecondLevel_Question_prompt = """
You will also get a sentence and a keyword which is the main theme of a sentence.
You are going to make 5 questions that encourage reading by using quotes from specific books as answers.
Questions should be about a keyword and should be deep, thought-provokable.
For example, if the text is "4.3 전쟁으로 인해 고통받는 사람들의 삶" and the keyword is "사람", then questions should be like these, "큰 고통 속에서도 인간의 존엄을 지키는 모습을 그린 문장 중 가장 기억에 남는 것은 무엇인가요?" or "고통스러운 상황 속에서도 서로를 위로하고 지지한 사람들의 모습을 그린 문장은 무엇인가요?".

Here’s how you should make questions:
1. you have to translate sentence and keyword to English.
2. Create 5 questions following the direction.
    The questions should be designed in a way that even if the reader doesn’t know the exact sentence, they can still reflect on the keyword.
    Questions shoue be possible to answer in quotes form.
        

This is precaution what you should be careful for:
- Just tell me the Questions, no small talk.

Here is the text and keyword.
text : {{text}}
keyword : {{keword}}
"""
