# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty

import random

print("Vyberte obtížnost:")
print("1. Snadná (7 životů)")
print("2. Střední (5 životů)")
print("3. Těžká (3 životy)")

difficulty = input("Zadejte číslo obtížnosti (1, 2 nebo 3): ").strip()

if difficulty == "1":
    lives = 7
elif difficulty == "2":
    lives = 5
elif difficulty == "3":
    lives = 3
else:
    print("Neplatná volba, nastavuje se střední obtížnost.")
    lives = 5

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
    word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
    lives = 5 # sample data, normally the lives should be chosen based on the difficulty

def load_words(file_path):
    words = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            city = line.split(" | ")[1]  # Získá název země před spojovníkem
            words.append(city.strip())
    return words

words = load_words("countries-and-capitals.txt")
word_to_guess = random.choice(words).lower()
    
    
# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"

game_state = ["_" for _ in word_to_guess]
already_tried_letters = []

ascii_art = [
    """
      -----
      |   |
      |   O
      |  /|\\
      |  / \\
      -
    """,
    """
      -----
      |   |
      |   O
      |  /|\\
      |  / 
      -
    """,
    """
      -----
      |   |
      |   O
      |  /|\\
      |
      -
    """,
    """
      -----
      |   |
      |   O
      |  /|
      |
      -
    """,
    """
      -----
      |   |
      |   O
      |
      |
      -
    """,
    """
      -----
      |   |
      |
      |
      |
      -
    """
]
print(ascii_art[7 - lives])

# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions

while lives > 0 and "_" in game_state:
    # Zobrazení aktuálního stavu hry
    print("\n" + " ".join(game_state))
    print(ascii_art[7 - lives])  # Zobrazení grafiky dle zbývajících životů
    print(f"Životy: {lives}")
    print(f"Špatné pokusy: {', '.join(already_tried_letters)}")

    guess = input("Hádej písmeno nebo napiš 'quit': ").strip().lower()
    if guess == "quit":
        print("Hra ukončena. Nashledanou!")
        break
    
    
# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
# this list will contain all the tried letters


    if guess in already_tried_letters:
        print("Toto písmeno už bylo zkoušeno. Zkus jiné.")
        continue
    already_tried_letters.append(guess)
    

# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".

    if guess in word_to_guess:
        print("Správně!")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                game_state[index] = letter
    else:
        print("Špatně!")
        lives -= 1


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4

if "_" not in game_state:
    print(f"\nGratulujeme! Uhodl/a jsi celé slovo: {word_to_guess}")
else:
    print(ascii_art[0])  # Konečná grafika pro prohru
    print(f"Došly ti životy! Slovo bylo: {word_to_guess}")
    