MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    """Prints a report of remaining resources and total profits"""
    for k, v in resources.items():
        print(str(k) + ':' + str(v))
    print(f"Money: ${money:.2f}")


def make_drink():
    """Checks if there is enough resources for chosen beverage"""
    for quantity in resources:
        if resources[quantity] < MENU[menu_choice]['ingredients'][quantity]:
            return f"Sorry there is not enough {quantity}"
    return f"Please insert ${MENU[menu_choice]['cost']:.2f}:"


def insert_money():
    """Adds the coins entered and checks if enough money was deposited to pay for selected drink"""
    global money
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    money_added = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    # TODO: 6: Check if transaction is successful
    if money_added >= MENU[menu_choice]['cost']:
        change = money_added - MENU[menu_choice]['cost']
        money += MENU[menu_choice]['cost']
        # TODO: 7: Deduct resources and add money to profits
        deduct_items()
        return f"Here is ${change:.2f} in change.\nHere is your {menu_choice} ☕. Enjoy!"
        
    else:
        return "Sorry that's not enough money. Money refunded."


def deduct_items():
    """Detucts required drink ingredients from total available resources"""
    global resources
    for quantity in resources:
        resources[quantity] -= MENU[menu_choice]['ingredients'][quantity]


money = 0

machine_on = True

# TODO: 1: Prompt user to ask what they would like to do
while machine_on:
    # Enter drink choice or "report" to print report or "off" to turn off coffee machine
    menu_choice = input(" What would you like? (espresso/latte/cappuccino):").lower()
    if menu_choice == "off":
        # TODO: 2: Turn off Coffee machine by entering "off" to the prompt
        machine_on = False
    elif menu_choice == "report":
        # TODO: 3: Allow user to print a report of remaining supplies and profit
        print_report()
    elif menu_choice == "espresso" or menu_choice == "latte" or menu_choice == "cappuccino":
        # TODO: 4: Check if resources are sufficient
        print(make_drink())
        # TODO: 5: Process the coins
        print(insert_money())
    else:
        print("Please enter a valid selection")

