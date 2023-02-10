import sys
import requests
from bs4 import BeautifulSoup


def road_to_philosophy(page_title, pages_visited):
    URL = "https://en.wikipedia.org/wiki/" + page_title

    try:
        response = requests.get(URL)
        response.raise_for_status()  # if there's redirects, follow up
        soup = BeautifulSoup(response.content, "html.parser")
        page_title = soup.find(name="title").text.split(" - ")[0]
        all_links = soup.find(id="mw-content-text").select("p > a")

        if len(all_links) == 0:
            sys.exit("It leads to a dead end !")
        if page_title in pages_visited:
            sys.exit("It leads to an infinite loop !")
        if page_title == "Philosophy":
            print("Philosophy")
            return

        print(page_title)
        pages_visited.append(page_title)

        for link in all_links:
            href_value = link['href']
            if href_value.startswith('/wiki/') and not (href_value.startswith('/wiki/Help:') or href_value.startswith('/wiki/Wikipedia:')):
                next_search_term = href_value.split('/')[-1]
                road_to_philosophy(next_search_term, pages_visited)
                return

    except requests.exceptions.RequestException:
        sys.exit("It leads to a dead end !")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Pass in only one argument, use double quotes if necessary")
    initial_search_term = sys.argv[1].replace(' ', '_')

    pages_visited = []

    road_to_philosophy(initial_search_term, pages_visited)

    print((str(len(pages_visited)) + " roads from " +
          initial_search_term + " to philosophy"))
