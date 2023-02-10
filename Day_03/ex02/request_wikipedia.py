import requests
import json
import sys
import dewiki


def get_page_as_wikitext(page_id):
    API_ENDPOINT = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'parse',
        'pageid': page_id,
        'prop': 'wikitext',
        'format': 'json'
    }
    try:
        response = requests.get(API_ENDPOINT, params=params)
        data = json.loads(response.text)['parse']['wikitext']['*']
        return data
    except requests.exceptions.RequestException:
        sys.exit("An error occurred trying to make the call to MediaWiki API")


def dewiki_wikitext(text):
    return dewiki.from_string(text).strip()

def get_page_id(search_term):
    API_ENDPOINT = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'titles': search_term,
        'prop': 'extracts',
        'redirects': True,
        'explaintext': 2
    }
    try:
        response = requests.get(API_ENDPOINT, params=params)
        page_id = list(json.loads(response.text)['query']['pages'].keys())[0]
        
        return page_id
    except requests.exceptions.RequestException:
        sys.exit("An error occurred while searching the term in the Wikipedia API")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Error: pass one string to be used as the search term.")

    search_term = sys.argv[1].replace(' ', '_')

    page_id = get_page_id(search_term)

    wikitext = get_page_as_wikitext(page_id)
    
    dewikied_page = dewiki_wikitext(wikitext)
    
    output = open(search_term + ".wiki", 'w')
    output.write(dewikied_page)
