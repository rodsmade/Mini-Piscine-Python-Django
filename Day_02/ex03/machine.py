from beverages import Cappuccino, Chocolate, Coffee, HotBeverage, Tea
import random




class CoffeeMachine:
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def __init__(self) -> None:
            pass

        def description(self) -> str:
            return ("An empty cup?! Gimme my money back!")


    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")
    
    def __init__(self) -> None:
        self.serve_counter = 0
        self.repaired = True

    def repair(self):
        self.repair = True
        self.serve_counter = 0
        print("This machine has been repaired. Come again!\n")

    def serve(self, hot_beverage):
        if self.serve_counter < 10:
            random_options = [hot_beverage, self.EmptyCup]
            beverage_class = random.choice(random_options)
            self.serve_counter += 1
            return beverage_class()
        else:
            self.repaired = False
            raise self.BrokenMachineException


if __name__ == "__main__":
    machine = CoffeeMachine()
    beverage_classes = [Coffee, Tea, Cappuccino, Chocolate]

    try:
        for i in range(15):
            print("------------------------------------ Drink No.: ", i + 1, "\n", machine.serve(beverage_classes[i % 4]), '\n', sep="")
    except machine.BrokenMachineException as e:
        print(e)
    
    machine.repair()

    try:
        for i in range(15):
            print("------------------------------------ Drink No.: ", i + 1, "\n", machine.serve(beverage_classes[i % 4]), '\n', sep="")
    except machine.BrokenMachineException as e:
        print(e)