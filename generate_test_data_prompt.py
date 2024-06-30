import os
import asyncio
from Util.EnvironmentVariable import env
from Util.AsyncHttpRequest import Request
from Util.Util import get_random_id

API_MODEL = env("OPENAI_MODEL")
API_KEY = env("OPENAI_API_KEY")

prompt = open("./generate_test_data_prompt.md", "r").read()

async def generate_test_data(filename):
    f = open(f"./summary/{filename}", "r")
    summaries = list(eval(f.read()))
    f.close()

    messages = [
        {
            "role": "system",
            "content": "Your role is to create 10 transcripts that encompass the three summaries mentioned."
        },
        {
            "role": "user",
            "content": prompt.format(
                summaries=summaries
            )
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

    f = open("./transcript/{}".format(filename), "w")
    f.write(response)
    f.close()


def list_files(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            files.append(filename)
    return files

async def main():
    file_list = list_files("./summary")

    tasks = []
    for file_name in file_list:
        tasks.append(generate_test_data(file_name))

    chunk_size = 5
    for i in range(0, len(file_list), chunk_size):
        print(i, i + chunk_size)
        await asyncio.gather(*tasks[i:(i+chunk_size)])

asyncio.run(main())