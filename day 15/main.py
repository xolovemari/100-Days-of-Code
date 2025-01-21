from machine_info import resources
from machine_info import MENU

machine_on = True
resources['money'] = 0

while machine_on:

    def make_coffee(user_choice):
        ingredients = MENU[user_choice]['ingredients']
        price = MENU[user_choice]['cost']

        for ingredient, amount in ingredients.items():
            if amount > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return
            
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

        if total_money >= price:
            change = round(total_money - price, 2)
            resources['money'] += price
            print(f"Here is ${change} in change.")
        else:
            print("Sorry that's not enough money. Money refunded.")
            return
        
        for ingredient, amount in ingredients.items():
            resources[ingredient] -= amount

        print(f"Here is your {user_choice} ☕. Enjoy!") 

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${resources['money']:.2f}")
    elif user_choice == "off":
        print("Thanks for using!")
        machine_on = False
    elif user_choice in MENU:
        make_coffee(user_choice)
    else:
        print("Invalid input, please try again.")