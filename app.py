from flask import Flask  
from flask import jsonify 
from flask import request
from urllib.parse import urlparse
import requests


app = Flask(__name__)
if __name__ == "__main__":
    app.config['SERVER_NAME'] = 'wiki-search.com'
    app.run()


@app.route("/")
def wiki_search():
    subdomain = urlparse(request.url).hostname.split('.')[0]
    BASE_URL = 'https://en.wikipedia.org/w/api.php'

    PARAMS = {
    "action" : "query",
    "format" : "json",
    "generator" : "links",
    "gplnamespace" : 0,
    "gpllimit" : "max",
    "prop" : "info",
    "inprop" : "url",
    "titles" : subdomain
    }

    res = requests.get(BASE_URL, params=PARAMS)

    pages = res.json()['query']['pages']

    url_list = []

    for key in pages:
        url_list.append(res.json()['query']['pages'][key]['fullurl'])

    results = {
        "links" : url_list
    }

    return results



    
