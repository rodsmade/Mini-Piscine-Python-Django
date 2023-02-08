import requests
import json
import sys
import dewiki


def get_page_as_wikitext(page_title):
    API_ENDPOINT = "https://en.wikipedia.org/w/api.php?action=parse&page=" + page_title + "&prop=wikitext&format=json"
    
    try:
        response = requests.get(API_ENDPOINT)
        data = json.loads(response.text)['parse']['wikitext']['*']
        return data
    except requests.exceptions.RequestException:
        sys.exit("An error occurred trying to make the call to MediaWiki API")


def dewiki_wikitext(text):
    return dewiki.from_string(text).strip()

def search_for_page_title(search_term):
    API_ENDPOINT = "https://en.wikipedia.org/w/api.php?action=opensearch&search="
    try:
        response = requests.get(API_ENDPOINT + search_term)
        list_of_results = json.loads(response.text)[3]
        if len(list_of_results) == 0:
            sys.exit("No page matches the requested search term")
        else:
            return list_of_results[0].rsplit('/', 1)[-1]
    except requests.exceptions.RequestException:
        sys.exit("An error occurred while searching the term in the Wikipedia API")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Error: pass one string to be used as the search term.")

    search_term = sys.argv[1].replace(' ', '_')

    page_title = search_for_page_title(search_term)

    wikitext = get_page_as_wikitext(page_title)
    
    dewikied_page = dewiki_wikitext(wikitext)
    
    output = open(search_term + ".wiki", 'w')
    output.write(dewikied_page)
