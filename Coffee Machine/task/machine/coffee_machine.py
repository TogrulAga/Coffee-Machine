# Write your code here
class Coffee:
    def __init__(self, water: int = 0, milk: int = 0, beans: int = 0, price: int = 0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price


class CoffeeMachine:
    espresso = Coffee(water=250, beans=16, price=4)
    latte = Coffee(water=350, milk=75, beans=20, price=7)
    cappuccino = Coffee(water=200, milk=100, beans=12, price=6)
    cups_per_drink = 1

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_state(self) -> None:
        print()
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of beans")
        print(self.cups, "of disposable cups")
        print("$", self.money, " of money", sep='')

    def sell_coffee(self) -> None:
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        print()
        drink = None

        if coffee_type == "back":
            return
        elif coffee_type == "1":    # espresso
            drink = CoffeeMachine.espresso
        elif coffee_type == "2":  # latte
            drink = CoffeeMachine.latte
        elif coffee_type == "3":    # cappuccino
            drink = CoffeeMachine.cappuccino

        if self.water - drink.water < 0:
            print("Sorry, not enough water!")
            return
        elif self.milk - drink.milk < 0:
            print("Sorry, not enough milk!")
            return
        elif self.beans - drink.beans < 0:
            print("Sorry, not enough coffee beans!")
            return
        elif self.cups - CoffeeMachine.cups_per_drink < 0:
            print("Sorry, not enough disposable  cups!")
            return
        else:
            self.water -= drink.water
            self.milk -= drink.milk
            self.beans -= drink.beans
            self.cups -= CoffeeMachine.cups_per_drink
            self.money += drink.price

    def fill_machine(self) -> None:
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take_money(self) -> None:
        print(f"I gave you ${self.money}")
        self.money = 0

    def make_action(self) -> None:
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            self.sell_coffee()
        elif action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.print_state()
        elif action == "exit":
            exit()


def main():
    coffee_machine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)

    while True:
        coffee_machine.make_action()


main()
