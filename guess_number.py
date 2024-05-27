number = 2

guess = ""

guess_limit = 3

number_of_guesses = 0
out_of_guesses = False



while guess!= number and not(out_of_guesses):
    if number_of_guesses<guess_limit:
       guess = int(input("Guess the number: "))
       number_of_guesses += 1 
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose!")

else:
    print("You Win!")

    



