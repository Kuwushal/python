import random

number = random.randrange(0, 9)
guess = None



guess_limit = 3

number_of_guesses = 0
out_of_guesses = False



while guess != number and not out_of_guesses:
    if number_of_guesses < guess_limit:
        try:
            guess = int(input("Guess the number from 0 to 9: "))
            number_of_guesses += 1
        except ValueError:
            print("Please enter a valid integer.")
    else:
        out_of_guesses = True

if out_of_guesses and guess != number:
    print("You Lose!")
else:
    print("You Win!")

print("The number was " + str(number))