from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
reports = CoffeeMaker()
profit = MoneyMachine()

def coffee_machine(drink):
    if drink:
        if reports.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                reports.make_coffee(drink)
                return
            else:
                return
        else:
            return
    else:
        return


while True:
    user_choice = input(f"What would you like? {my_menu.get_items()}: ").lower()
    if user_choice == "report":
        reports.report()
        profit.report()
    elif user_choice == "off":
        print("Thanks for using!")
        break
    else:   
        drink = my_menu.find_drink(user_choice)

    if "report" not in user_choice:
        coffee_machine(drink)        
    