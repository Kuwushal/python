import random

def print_signs():
    signs = ['♜', '⚓', '♆', '❀']
    selected_signs = []

    print("Press Enter to reveal a sign.")
    
    for i in range(3):
        input("Press Enter!: ") 
        sign = random.choice(signs)
        selected_signs.append(sign)
        print(f"Sign {i+1}: {sign}")

    if selected_signs[0] == selected_signs[1] == selected_signs[2]:
        print(f"You win! You got {selected_signs[0]} {selected_signs[1]} {selected_signs[2]}")
    else:
        print(f"You lose! You got {selected_signs[0]} {selected_signs[1]} {selected_signs[2]}")


print_signs()