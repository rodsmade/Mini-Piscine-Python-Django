import requests
import json
import sys
import dewiki


def get_page_as_wikitext(page_title):
    API_ENDPOINT = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'parse',
        'page': page_title,
        'prop': 'wikitext',
        'format': 'json'
    }
    response = requests.get(API_ENDPOINT, params=params)
    if response.status_code != 200:
        print("request deu ruim")
        print(response.text)
        return None
    else:
        # print(response.text)
        data = json.loads(response.text)['parse']['wikitext']['*']
        return data


def dewiki_wikitext(text):
    return dewiki.from_string(text).strip()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: pass one string to be used as the search term.")
        sys.exit(-42)

    search_term = sys.argv[1]
    wikitext = get_page_as_wikitext(search_term)
    dewikied_page = dewiki_wikitext(wikitext)

    output = open(search_term + ".wiki", 'w')
    output.write(dewikied_page)
