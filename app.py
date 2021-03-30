from flask import Flask  
from flask import jsonify 
from flask import request
import requests


app = Flask(__name__, subdomain_matching=True)

if __name__ == "__main__":
    url = 'wiki-search.com:5000'
    app.config['SERVER_NAME'] = url
    app.run()


@app.route('/')
def wiki_search():
    BASE_URL = 'https://en.wikipedia.org/w/api.php'

    PARAMS = {
    "action" : "query",
    "format" : "json",
    "generator" : "links",
    "gplnamespace" : 0,
    "gpllimit" : "max",
    "prop" : "info",
    "inprop" : "url",
    "titles" : "ordinary"
    }

    res = requests.get(BASE_URL, params=PARAMS)

    pages = res.json()['query']['pages']

    url_list = []

    import pdb; pdb.set_trace()
    for key in pages:
        url_list.append(res.json()['query']['pages'][key]['fullurl'])

    results = {
        "links" : url_list
    }

    return results


    
