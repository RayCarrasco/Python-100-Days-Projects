import information

menu = information.MENU
resource = information.resources
money = 0
is_on = True


def off():
    global is_on
    is_on = False


def report():
    global resource
    print(f"\nWater: {resource['water']}"
          f"\nMilk: {resource['milk']}"
          f"\nCoffee: {resource['coffee']}"
          f"\nMoney: ${money}")


def manage_resources(p_ordered_bbr, p_total):
    global resource
    global money
    resource['water'] -= menu[p_ordered_bbr]['ingredients']['water']
    resource['coffee'] -= menu[p_ordered_bbr]['ingredients']['coffee']
    if 'milk' in menu[p_ordered_bbr]['ingredients']:
        resource['milk'] -= menu[p_ordered_bbr]['ingredients']['milk']
    money += menu[p_ordered_bbr]['cost']
    change = p_total - menu[p_ordered_bbr]['cost']
    print(f"Here is ${change:.2f} in change.")


def order_beverage(ordered_bbr):
    order_proceeds = True
    total = 0
    if 'milk' in menu[ordered_bbr]['ingredients']:
        if resource['milk'] < menu[ordered_bbr]['ingredients']['milk']:
            order_proceeds = False
            print("Sorry there is not enough milk.")
    elif resource['water'] < menu[ordered_bbr]['ingredients']['water']:
        order_proceeds = False
        print("Sorry there is not enough water.")
    elif resource['coffee'] < menu[ordered_bbr]['ingredients']['coffee']:
        order_proceeds = False
        print("Sorry there is not enough coffee.")
    else:
        print("Enough resources")

    if order_proceeds:
        print("Insert coins.")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        if total < menu[ordered_bbr]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            order_proceeds = False

    if order_proceeds:
        manage_resources(ordered_bbr, total)
        print(f"Here is your {ordered_bbr} ☕, Enjoy!.")


functions = {
    'report': report,
    'off': off,
}


def coffee_machine():
    command = input("\nWhat would you like? (espresso/latte/cappuccino):")
    if command in functions:
        functions[command]()
    elif command in menu:
        order_beverage(command)


while is_on:
    coffee_machine()
print("\nPower off")
