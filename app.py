from flask import Flask  
from flask import jsonify 
from flask import request
import requests


app = Flask(__name__, subdomain_matching=True)

print("Please enter a search term:")

search_term = input()

if __name__ == "__main__":
    url = 'wiki-search.com:5000'
    app.config['SERVER_NAME'] = url
    app.run()


@app.route('/', subdomain = search_term)
def wiki_search(search_term):
    BASE_URL = 'https://en.wikipedia.org/w/api.php'

    PARAMS = {
    "action" : "query",
    "format" : "json",
    "generator" : "links",
    "gplnamespace" : 0,
    "gpllimit" : "max",
    "prop" : "info",
    "inprop" : "url",
    "titles" : search_term
    }

    res = requests.get(BASE_URL, params=PARAMS)

    results = res["query"]["pages"][0]["fullurl"]

    # results = {
    #     "links" : 
    # }

    return results


    
