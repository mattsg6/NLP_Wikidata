import os
import openai
import requests
import sseclient
import json

endpoint = 'https://api.openai.com/v1/completions'

input = {
    "model":"text-davinci-003",
    "prompt":"Say this is a test",
    "max_tokens":7,
    "temperature":0,
    "stream": True
}

headers = {
    'Accept': 'text/event-stream',
    'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']
}

response = requests.post(endpoint, stream = True, headers=headers, json=input)
sseClient = sseclient.SSEClient(response)


for event in sseClient.events():
    if event.data != '[DONE]':
        print(json.loads(event.data)['choices'][0]['text'], end='', flush=True)