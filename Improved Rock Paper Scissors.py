# Best 3 out of 5 Rock, Paper, Scissors w/ option to restart.

import random

# These variables tally the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

rock = '''
ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computerOptions = [rock, paper, scissors]

while True:
  print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
  while True:
    playerChoice = input('What do you choose? Type 1 for rock, 2 for paper, or 3 for scissors.\n')
    if playerChoice == "1":
      print('\nYou chose...' + rock)
      playerChoice = rock
      break
    elif playerChoice == "2":
      print('\nYou chose...' + paper)
      playerChoice = paper
      break
    elif playerChoice == "3":
      print('\nYou chose...' + scissors)
      playerChoice = scissors
      break
    else:
      print("Please make a valid selection.\n")
      continue

  computerChoice = random.choice(computerOptions)
  print("The computer chose..." + computerChoice)

  if computerChoice == playerChoice:
    print("It's a tie...")
    ties += 1
  elif computerChoice == rock and playerChoice == scissors:
    print("You lose!")
    losses += 1
  elif computerChoice == rock and playerChoice == paper:
    print("You win!")
    wins += 1

  elif computerChoice == scissors and playerChoice == paper:
    print("You lose!")
    losses += 1
  elif computerChoice == scissors and playerChoice == rock:
    print("You win!")
    wins += 1

  elif computerChoice == paper and playerChoice == rock:
    print("You lose!")
    losses += 1
  elif computerChoice == paper and playerChoice == scissors:
    print("You win!")
    wins += 1

  # Option to restart/reset the game
  if wins == 3:
      print("Congratulations! You win the match!")
      again = (input('\nPlay again?\n')).lower()
      if again == 'y' or again == 'yes' or again == "":
              wins = 0
              losses = 0
              ties = 0
              continue
      else:
          break
  if losses == 3:
      print("Game Over!")
      again = (input('\nPlay again?\n')).lower()
      if again == 'y' or again == 'yes' or again == "":
              wins = 0
              losses = 0
              ties = 0
              continue
      else:
          break

print("\nGoodbye.")
