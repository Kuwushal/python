print("Welcome to the game!")

playgame = ((input("Do you want to play this game?: "))).lower()


if playgame != "yes":
    quit()

print("Okay! Lets get in")
score = 0

answer = input("What does RAM stand for?: ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Japan?: ").lower()
if answer == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the founder of Apple?: ").lower()
if answer == "steve jobs":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

try:

    answer = int(input("How many times has Australia won cricket World Cup?: "))
    if answer == 6:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
except ValueError:
    print("Incorrect! Enter a valid integer")

print("You got " + str(score) + " questions correct!")