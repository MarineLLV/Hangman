import random
import hangman_words as words
import hangman_art as art


end_of_game = False
chosen_word = random.choice(words.word_list)
# print(f"For testing only --> The word is: {chosen_word}")

# Keep track of the number of lives left
lives = len(art.stages) - 1

# Import logo art
print(art.logo)

# Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Chek guessed letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If no match between letter and word, reduce the lives by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose 1 life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # print the ASCII art from 'stages' that corresponds to the current number of lives the user has remaining
    print(art.stages[lives])
