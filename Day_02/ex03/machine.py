import beverages


class EmptyCup(beverages.HotBeverage):
    def __init__(self) -> None:
        self.name = "empty cup"
        self.price = 0.90

    def description(self) -> str:
        return ("An empty cup?! Gimme my money back!")


class BrokenMachineException(Exception):
    def __init__(self) -> None:
        super().__init__("This coffee machine has to be repaired.")


class CoffeeMachine:
    def __init__(self) -> None:
        pass

    def test_machine(self):
        raise BrokenMachineException

    def repair(self):
        print("This machine is under repair. Please come again later!")

    def serve(self, hot_beverage):
        print("Serving a cup of {} for {:.2f}".format(hot_beverage.description(), hot_beverage.price))


if __name__ == "__main__":
    machine = CoffeeMachine()
    empty_cup = EmptyCup()
    print(empty_cup)

    try:
        machine.test_machine()
    except BrokenMachineException as e:
        print(e)

    coffee = beverages.Coffee()
    machine.serve(coffee)

    tea = beverages.Tea()
    machine.serve(tea)
    
    chocolate = beverages.Chocolate()
    machine.serve(chocolate)

    machine.repair()