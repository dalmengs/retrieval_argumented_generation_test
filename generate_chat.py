import asyncio
from Util.EnvironmentVariable import env
from Util.AsyncHttpRequest import Request
from Util.Util import get_random_id
from topics import topics

API_MODEL = env("OPENAI_MODEL")
API_KEY = env("OPENAI_API_KEY")

"""
    `topics.py`에 정의되어 있는 주제로 대화를 만듭니다.
"""

async def generate_chat(topic):
    messages = [
        {
            "role": "system",
            "content": "Your role is to make conversation transcript between two people, Naly(AI) and User(human)."
        },
        {
            "role": "user",
            "content": open("./generate_chat_prompt.md", "r").read().format(topic=topic)
        }
    ]

    response = await Request.post(
        url='https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {API_KEY}"
        },
        data={
            "model": API_MODEL,
            "messages": messages,
        }
    )
    response = response.json()["choices"][0]["message"]["content"]

    chat_id = get_random_id()
    f = open("./chat/{}.txt".format(chat_id), "w")
    f.write(response)
    f.close()

async def main():
    tasks = []
    for topic in topics:
        tasks.append(generate_chat(topic))

    chunk_size = 5
    for i in range(0, len(topics), chunk_size):
        await asyncio.gather(*tasks[i:(i+chunk_size)])

asyncio.run(main())