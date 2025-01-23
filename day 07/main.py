import random
from words import words
from stages import stages

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

chosen_word = random.choice(words)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"\n*************************** {lives}/6 LIVES LEFT ***************************")
    display = ""
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("\nYou've already guessed " + guess)
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"            
    print(display)   
    
    if guess not in chosen_word:
        lives -= 1
        print("\nYou guessed " + guess + ", that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("\n*************************** YOU LOSE ***************************")
    
    if "_" not in display:
        game_over = True
        print("\n*************************** YOU WIN ***************************")
    
    print(stages[lives])
