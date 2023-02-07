import requests, json, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: pass one string to be used as the search term.")
        sys.exit(-42)
    search_term = sys.argv[1]

    response = requests.get("https://en.wikipedia.org/w/api.php?action=parse&page=Fleet_foxes&format=json")
    print(response.content.decode('utf-8'))

    # só abrir o arquivo se der bom, ou seja, não criar se  parameter absence, wrong parameter, invalid request, information not found, server problem or any other problem
    # open(search_term + ".wiki", 'w')