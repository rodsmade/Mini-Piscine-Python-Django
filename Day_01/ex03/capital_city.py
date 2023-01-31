import sys

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def capital_city():
    if (len(sys.argv) != 2):
        return
    elif (sys.argv[1] not in states.keys()):
        print("Unknown state")
    else:
        print(capital_cities[states[sys.argv[1]]])

    return


if __name__ == '__main__':
    capital_city()
