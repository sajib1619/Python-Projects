import random

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100. Can you guess it?")
n = random.randint(1, 100)
cnt = 0
while True:
    guess = input("Enter your guess: ")
    cnt += 1
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    else:
        guess = int(guess)
    
    if guess == 0:
        print("Guess number Above 0")
        continue

    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break

print(f"You guessed the number in {cnt} attempts.")