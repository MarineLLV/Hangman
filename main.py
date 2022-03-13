import random
# Pick a random word and check answers

word_list = ["algorithm", "binary", "coplanar", "deviation", "exponential", "fibonacci", "gaussian", "hexadecimal", "increment", "joule", "kilometer", "logarithmic", "modulo", "number", "operator", "property", "quadratic", "range", "square", "transpose", "unit", "vector"]
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
