from flask import Blueprint, render_template, redirect, url_for, request
import requests
from scripts.wikidata import wikidata_query

api = Blueprint('api', __name__)

@api.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@api.route('/results')
def res():
    # TEMP: DATA WILL BE ROUTED DIFFERENTLY
    endpoint_url = "https://query.wikidata.org/sparql"

    query = """PREFIX wd: <http://www.wikidata.org/entity/>
                PREFIX wdt: <http://www.wikidata.org/prop/direct/>

                SELECT ?film ?cinematographer WHERE {
                ?films wdt:P31 wd:Q11424 ;
                        wdt:P57 wd:Q7374 ;
                        wdt:P344 ?cinematographers .
                ?films rdfs:label ?film .
                ?cinematographers rdfs:label ?cinematographer .
                FILTER (lang(?film) = "en" && lang(?cinematographer) = "en")
                }
    """

    question = 'What are the names of all the films directed by Alfred Hitchcock and who was the cinematographer for each?'

    payload = wikidata_query(endpoint_url=endpoint_url, query=query)

    return render_template('results.html', res=payload, question=question)

@api.route('/question', methods=['POST'])
def process():
    print(request.json)

    return url_for('api.res')