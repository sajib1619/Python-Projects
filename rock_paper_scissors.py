import random

list = ["rock", "paper", "scissors"]
a = 0
b = 0
while True:
    user_input = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user_input == "exit":
        print("Thanks for playing! Goodbye!")
        break
    
    if user_input not in list:
        print("Invalid input. Please try again.")
        continue
    
    computer_choice = random.choice(list)
    print(f"Computer chose: {computer_choice}")
    
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissors" and computer_choice == "paper"):
        print("You win!") 
        a += 1  
    else:
        print("Computer wins!")
        b += 1

print(f"Final Score - You: {a}, Computer: {b}")
    