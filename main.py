import random
# Pick a random word and check answers

word_list = ["algorithm", "binary", "coplanar", "deviation", "exponential", "fibonacci", "gaussian", "hexadecimal", "increment", "joule", "kilometer", "logarithmic", "modulo", "number", "operator", "property", "quadratic", "range", "square", "transpose", "unit", "vector"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
