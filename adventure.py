game_points = 0

name = input("Enter your name: ")

print("Welcome adventurer", name, ", Do good deeds to earn the points.")

answer = input("There are cries of help coming from your right and there's a treasure box full of golds on your left, Do you go to your right or left? (right/left) : ")

if answer.lower() == "right":
    game_points +=1
    print("Good Job! You saved some people and earned a point.")

elif answer.lower() == "left":
    print("You are selfish, the treasure box was a trap.")
    print("Your score is ", game_points)
    quit()

else:
    print("Not a valid answer, You lose!")
    print("Your score is ", game_points)
    quit()

answer = input("The people you saved guide you to a hidden vllage. Do you follow them? follow/explore: ")

if answer.lower() == "follow":
    print("Great! You found a hidden village with kind people and they repay you with some supplies for your journey and help with the direction.")
    game_points += 1

elif answer.lower() == "explore":
    print("You chose to explore on your own and got lost in the forest. You Lose!")
    game_points -=1
    print("Your score is ", game_points)
    quit()

else:
    print("Not a valid answer, You lose!")
    print("Your score is ", game_points)
    quit()

answer = input("Do you want to stay in the village for the night or continue your journey? (stay/continue): ")

if answer.lower() == "stay":
    game_points += 1
    print("You stayed in the village and had a restful night. The villagers provided you with valuable information about the forest. You earned another point.")

        
elif answer.lower() == "continue":
    game_points -=1
    print("You decided to continue your journey through the night. It's dark and dangerous, and you lose your way. You lose the game.")
    print(f"Your score is", game_points)
    quit()

else:
    print("Not a valid answer. You lose!")
    print(f"Your score is", game_points)
    quit()


print("With the villagers' guidance, you learn about the Demon King terrorizing the land. You decide to face him and end his reign of terror.")

answer = input("Do you prepare yourself with the supplies given by the villagers or rush to face the Demon King immediately? (prepare/rush): ")

if answer.lower() == "prepare":
    game_points += 1
    print("You carefully prepare yourself, using the supplies and information provided by the villagers. You feel ready to face the Demon King.")


elif answer.lower() == "rush":
    game_points -= 1
    print("You rush to face the Demon King without preparation. The Demon King overpowers you, and you lose the battle. You lose the game.")
    print("Your score is ", game_points)
    quit()

else:
    print("Not a valid answer. You lose!")
    print("Your score is ", game_points)
    quit()


print("Your score is ", game_points)




