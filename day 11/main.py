import random
from art import logo

def adjust_for_ace(deck, total):
    while total > 21 and 11 in deck:
        deck[deck.index(11)] = 1
        total -= 10
    return total

def blackjack():
    print(logo)

    while True:
        start_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
        if start_game == 'n':
            print("Goodbye!")
            return
        elif start_game != 'y':
            print("Invalid input, please try again.")
            continue

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        your_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]
        total_user = sum(your_cards)
        total_comp = sum(computer_cards)

        print(f"Your cards: {your_cards}, current score: {total_user}")
        print(f"Computer's first card: {computer_cards[0]}")

        if total_user == 21 or total_comp == 21:
            if total_user == total_comp:
                print(f"It's a draw! Both got Blackjack!")
            elif total_user == 21:
                print(f"Blackjack! You win! Your cards: {your_cards}, final score: {total_user}.")
            else:
                print(f"Blackjack! You lose. Computer's cards: {computer_cards}, final score: {total_comp}.")
            return

        while total_user < 21:
            total_user = adjust_for_ace(your_cards, total_user)
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_choice == 'y':
                new_card = random.choice(cards)
                your_cards.append(new_card)
                total_user += new_card
                print(f"Your cards: {your_cards}, current score: {total_user}")
                print(f"Computer's first card: {computer_cards[0]}")
            elif user_choice == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if total_user <= 21:
            print("Computer's turn...")
            while total_comp < 17 and total_comp < 21:
                new_card = random.choice(cards)
                computer_cards.append(new_card)
                total_comp += new_card
                total_comp = adjust_for_ace(computer_cards, total_comp)

        print(f"Your final hand: {your_cards}, final score: {total_user}")
        print(f"Computer's final hand: {computer_cards}, final score: {total_comp}")

        if total_user > 21:
            print("You went over. You lose!")
        elif total_comp > 21:
            print("Computer went over. You win!")
        elif total_user == total_comp:
            print("It's a draw!")
        elif total_user > total_comp:
            print("You win!")
        else:
            print("You lose.")

        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            print("Goodbye!")
            return
        
blackjack()
