import sys
import requests
from bs4 import BeautifulSoup

def find_first_link_in_page(page_title):
    URL = "https://en.wikipedia.org/wiki/" + page_title
    
    try:
        response = requests.get(URL)
    except requests.exceptions.RequestException:
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    all_links = soup.find(id="mw-content-text").select("p > a")

    if len(all_links) == 0:
        return None

    for item in all_links:
        attributes = str(item).split(' ')
        for attribute in attributes:
            if attribute.startswith('href'):
                next_page_title = attribute.split('=')[1]
                print("next page title:", next_page_title.rsplit('/', 1)[-1])
                return next_page_title.rsplit('/', 1)[-1]

    return None
    

if __name__ == "__main__":
    stop_loop = False
    pages_visited = []
    
    count = 0
    
    if len(sys.argv) != 2:
        sys.exit("Pass in only one argument, use double quotes if necessary")
    
    page_title = sys.argv[1].replace(' ', '_')
    
    while not stop_loop:
        pages_visited.append(page_title)
        first_link_referenced_in_page = find_first_link_in_page(page_title)
        
        if not first_link_referenced_in_page:
            sys.exit("It leads to a dead end !")
        if first_link_referenced_in_page in pages_visited:
            sys.exit("It leads to an infinite loop !")
        
        print(page_title)
        page_title = first_link_referenced_in_page
        count += 1
        if count == 3:
            break