import beverages

class CoffeeMachine:
    def __init__(self) -> None:
        pass

class EmptyCup(beverages.HotBeverage):
    def __init__(self) -> None:
        self.name = "empty cup"
        self.price = 0.90
    
    def description(self) -> str:
        return ("An empty cup?! Gimme my money back!")


if __name__ == "__main__":
    empty_cup = EmptyCup()
    print(empty_cup)
