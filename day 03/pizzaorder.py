print("Welcome to the Python Pizza Deliveries!")
size  =  input("What size pizza do you want? S, M OR L: ")
if size not in ['S', 'M', 'L']:
    print("Please type a valid size of pizza.")
    exit()
    
total = 0

if size == 'S':
    total = 15
elif size == 'M':
    total = 20
elif size == 'L':
    total = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == 'Y':
    total += 1

print(f"Your final bill is: ${total}")