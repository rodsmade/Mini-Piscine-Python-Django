class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self) -> str:
        return ("Just some hot water in a cup.")

    def __str__(self) -> str:
        hot_beverage_to_string = ""
        hot_beverage_to_string += "name : " + self.name + "\n"
        hot_beverage_to_string += "price : " + \
            "{:.2f}".format(self.price) + "\n"
        hot_beverage_to_string += "description : " + self.description()
        return (hot_beverage_to_string)


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.4

    def description(self) -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.5

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino (HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"


if __name__ == "__main__":
    hot_water = HotBeverage()
    print(hot_water, "\n")

    coffee = Coffee()
    print(coffee, "\n")

    tea = Tea()
    print(tea, "\n")

    chocolate = Chocolate()
    print(chocolate, "\n")

    cappuccino = Cappuccino()
    print(cappuccino, "\n")
