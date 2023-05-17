import requests
from dotenv import dotenv_values

endpoint = 'https://api.openai.com/v1/completions'

input = {
    "model":"text-davinci-003",
    "prompt":"Hello",
    "max_tokens":7,
    "temperature":0,
    "stream": True
}

headers = {
    'Accept': 'text/event-stream',
    'Authorization': 'Bearer ' + dotenv_values('.env')['OPENAI_API_KEY']
}

response = requests.post(endpoint, stream = True, headers=headers, json=input)
print(response.json())