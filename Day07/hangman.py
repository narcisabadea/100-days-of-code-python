# Implement the Hangman game.

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
display = []
end_of_game = False

lives = len(stages) - 1

for _ in range(len(chosen_word)):
    display += '_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print('Lives left:', lives)
        if lives == 0:
            end_of_game = True
            print("You lose. The words was", chosen_word)


    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win")

    
