def go():
    with open("numbers.txt", "r") as file:
        contents = file.read()
        numbers = contents.split(",")
        for number in numbers:
            print(number.strip())


if __name__ == '__main__':
    go()
