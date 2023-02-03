class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self) -> str:
        return ("Just some hot water in a cup.")
    
    def __str__(self) -> str:
        hot_beverage_to_string = ""
        hot_beverage_to_string += "name : " + self.name + "\n"
        hot_beverage_to_string += "price : " + "{:.2f}".format(self.price) + "\n"
        hot_beverage_to_string += "description : " + self.description()
        return (hot_beverage_to_string)

if __name__ == "__main__":
    hot_water = HotBeverage()
    print(hot_water)