import random

#define roll function
def roll():
    n = random.randint(1, 6)
    return n
while True:
    players = input("Enter the number of players to play the game.(2-4): ")
    #print(type(players))

    #check if input is right
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Enter a number from 2 to 4.")
    else:
        print("Invalid input.")

max_score = 50
players_score = [0 for _ in(range(players))]
winner = -1

while True:
    for i in range(players):
        curr_score = 0
        print(f"Its player {i+1}'s turn..")
        while True:
            ans = input("Would you like to roll the dice? (y/n): ").lower()
            if ans == 'n':
                players_score[i] += curr_score
                break
            elif ans != 'y':
                print("Enter y or n")
                continue

            num = roll()
            if num == 1:
                print("Bad luck!!")
                break
            else:
                curr_score += num
            
            print(f"Your current score is: {players_score[i]+curr_score}")
        
        if players_score[i] >= max_score:
            winner = i+1
            break
    if winner != -1:
        break

print("")
print("AND THE WINNER IS: PLAYER NUMBER ", winner)