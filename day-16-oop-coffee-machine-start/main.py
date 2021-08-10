from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def report():
    coffee_maker.report()
    money_machine.report()


def off():
    global is_on
    is_on = False


command = {
    "report": report,
    "off": off,
}


is_on = True
while is_on:
    entered_command = input(f"What would you like? {menu.get_items()}: ")
    if entered_command in command:
        command[entered_command]()

    beverage = menu.find_drink(entered_command)
    if beverage is not None and coffee_maker.is_resource_sufficient(beverage):
        if money_machine.make_payment(beverage.cost):
            coffee_maker.make_coffee(beverage)
