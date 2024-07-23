import random

def print_signs():
    signs = ['+', '-', '*', '/']
    selected_signs = []

    print("Press Enter to reveal a sign.")
    
    for i in range(3):
        input("Press Enter!: ") 
        sign = random.choice(signs)
        selected_signs.append(sign)
        print(f"Sign {i+1}: {sign}")

    if selected_signs[0] == selected_signs[1] == selected_signs[2]:
        print("You win! All three signs are the same.")
    elif len(set(selected_signs)) == 3:
        print("You lose! All three signs are different.")
    else:
        print("Neither win nor lose. Try again.")

print_signs()
