from art import logo

print(logo)

bidders = {}

def find_highest_bidder(bid_dictionary): 
    highest_bid = 0
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidders[name] = price
    should__continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should__continue == "no":
        find_highest_bidder(bidders)
        break;
    elif should__continue == "yes":
        print("\n" * 20)

