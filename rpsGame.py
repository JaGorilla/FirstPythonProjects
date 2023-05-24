# Best 3 out of 5 Rock, Paper, Scissors w/ option to restart.
import random, sys

print("ROCK, PAPER, SCISSORS")
print()
print("Best out of five wins.")

# These variables tally the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:
    print()
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    print()
    while True:  # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        print()
        if playerMove == "q":
            sys.exit()  # Quit the program.
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of r, p, s, or q.")

    # Display what the player chose:
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Display and tally the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
        print()
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
        print()
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
        print()
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
        print()
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
        print()
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
        print()
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses = losses + 1
        print()
    # Option to restart/reset the game
    if wins == 3:
        print("Congratulations! You win the match!")
        print("Play again?")
        ans = input()
        if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
            wins = 0
            losses = 0
            ties = 0
            continue
        elif ans == "":
            print()
            print("Type either [y]es or [n]o.")
            ans = input()
            if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
                wins = 0
                losses = 0
                ties = 0
                continue
            else:
                break
        else:
            break
    if losses == 3:
        print("Game Over!")
        print("Play again?")
        ans = input()
        if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
            wins = 0
            losses = 0
            ties = 0
            continue
        elif ans == "":
            print()
            print("Type either [y]es or [n]o.")
            ans = input()
            if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
                wins = 0
                losses = 0
                ties = 0
                continue
            else:
                break
        else:
            break
print()
print("Goodbye.")
