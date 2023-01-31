def my_var():
    print("42 has a type " + str(type(42)))
    print("42 has a type " + str(type("42")))
    print("quarante-deux has a type " + str(type("quarante-deux")))
    print("42.0 has a type " + str(type(42.0)))
    print("True has a type " + str(type(True)))
    print("[42] has a type " + str(type([42])))
    print("{42: 42} has a type " + str(type({42: 42})))
    print("(42,) has a type " + str(type((42,))))
    print("set() has a type " + str(type(set())))
    return


if __name__ == '__main__':
    my_var()
