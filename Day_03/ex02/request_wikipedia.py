import requests, json, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: pass one string to be used as the search term.")
        sys.exit(-42)
    print(sys.argv[1])