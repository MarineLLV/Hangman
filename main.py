import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["algorithm", "binary", "coplanar", "deviation", "exponential", "fibonacci", "gaussian", "hexadecimal", "increment", "joule", "kilometer", "logarithmic", "modulo", "number", "operator", "property", "quadratic", "range", "square", "transpose", "unit", "vector"]
chosen_word = random.choice(word_list)
print(f"For testing only --> The word is: {chosen_word}")
# Keep track of the number of lives left
lives = 6

# Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Chek guessed letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If no match between letter and word, reduce the lives by 1
    if guess not in chosen_word:
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
    print(stages[lives])
