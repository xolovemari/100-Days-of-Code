try:
    bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

    if tip not in [10, 12, 15]:
        print("Invalid amount of tip. Please choose 10, 12, or 15.")
        exit()

    people = int(input("How many people to spit the bill?"))
    if people <= 0:
            print("Number of people must be greater than 0.")
            exit()

    total = (bill + (tip / 100 * bill)) / people
    total = round(total, 2)

    print(f"Each person should pay: ${total}")
    
except ValueError:
    print("Invalid input. Please enter numbers only.")