# NLP_Wikidata

## About Wikifilm

Wikifilm uses the Natural Language Processing of OpenAI and the reliable data of Wikidata to allow users to ask questions about films, actors, directors, producers, etc. and receive true (or almost true) results.

## Virtual Environment and Dependencies

Create a virtual environment and install the dependencies in the requirements.txt file.

```
# Create virutal environment
python -m venv ./<name-of-virtalenv>

# Activate virtual environment
source <name-of-virtualenv>/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Run Flask app

In the main directory, run the following command:

```
# Start app
python app.py
```

## .env

You must have access to OpenAI's API. Generate an API key and store it in a .env file as follows:

```
OPENAI_API_KEY = <key>
```
