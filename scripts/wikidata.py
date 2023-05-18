import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?filmLabel WHERE {
  ?film wdt:P31 wd:Q11424 ;
        wdt:P57 wd:Q522057 ;
        wdt:P161 wd:Q238464 ;
        rdfs:label ?filmLabel .
  FILTER (lang(?filmLabel) = "en")
}
"""


def get_results(endpoint_url, query):
    user_agent = "Wikidata-AI-app/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def wikidata_query(endpoint_url, query):
    results = get_results(endpoint_url, query)

    format = []
    for result in results["results"]["bindings"]:
        keys = list(result.keys())
        temp = {}
        for k in keys:
            temp[k] = result[k]['value']

        format.append(temp)

    return format
