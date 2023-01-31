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
    elif (sys.argv[1] not in capital_cities.values()):
        print("Unknown capital city")
    else:
        state_code = list(capital_cities.keys())[list(capital_cities.values()).index(sys.argv[1])]
        print(list(states.keys())[list(states.values()).index(state_code)])

    return


if __name__ == '__main__':
    capital_city()
