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


def capital_city(state):
    if (state not in states.keys()):
        return ("Unknown state")
    else:
        return (capital_cities[states[state]])


def state(capital):
    if (capital not in capital_cities.values()):
        return ("Unknown capital city")
    else:
        all_capitals = list(capital_cities.values())
        index_of_capital = all_capitals.index(capital)
        return (list(states.keys())[index_of_capital])


def all_in():
    if len(sys.argv) != 2:
        return
    terms = sys.argv[1].split(",")
    stripped_terms = []
    for term in terms:
        stripped_terms.append(term.strip(' '))

    no_double_spaces = []
    for element in stripped_terms:
        while '  ' in element:
            element = element.replace('  ', ' ')
        no_double_spaces.append(element)

    for element in no_double_spaces:
        capitalized = str(element).title()
        if capitalized in capital_cities.values():
            print(capitalized, "is the capital of", state(capitalized))
        elif capitalized in states.keys():
            print(capital_city(capitalized), "is the capital of", capitalized)
        elif element != '':
            print(element, "is neither a capital city nor a state")

    return


if __name__ == '__main__':
    all_in()
