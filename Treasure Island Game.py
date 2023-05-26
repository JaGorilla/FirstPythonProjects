# Treasure Island Game
while True:
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.\n")

  direction = (input('\nDo you want to start exploring to the left or right?\n')).lower()
  if direction != 'left':
    print('\nYou fell into a hole full of gators. Game over.')
    ans = (input("\nPlay again?\n")).lower()
    if ans == "yes" or ans == "y" or ans == "":
      print()
      continue
    else:
      break
  elif direction == 'left':
    action = (input('''\nYou find a wide river. Do you swim across or look for a crossing further downstream? Enter either "swim" or "walk".\n''')).lower()
    if action != 'walk':
      print('\nOuch. You were eaten by a gator. Game over.')
      ans = (input("\nPlay again?\n")).lower()
      if ans == "yes" or ans == "y" or ans == "":
        print()
        continue
      else:
        break
    elif action == 'walk':
      door = (input('''\nYou come across an abandoned building with three different colored doors. Which door do you open? Red, yellow, or blue?\n''')).lower()
      if door == 'red':
        print('''\nOuch. Samuel L. Jackson was waiting for you. Game over.''')
        ans = (input("\nPlay again?\n")).lower()
        if ans == "yes" or ans == "y" or ans == "":
          print()
          continue
        else:
          break
      elif door == 'blue':
        print('''\nOuch. That door was booby-trapped with an explosive. Game over.''')
        ans = (input("\nPlay again?\n")).lower()
        if ans == "yes" or ans == "y" or ans == "":
          print()
          continue
        else:
          break
      elif door == 'yellow':
        print('''
  *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  \nYou win! You found the treasure!''')
        ans = (input("\nPlay again?\n")).lower()
        if ans == "yes" or ans == "y" or ans == "":
          print()
          continue
        else:
          break
      else:
        print('\nThe door you chose doesn\'t exist. Game over.')
        ans = (input("\nPlay again?\n")).lower()
        if ans == "yes" or ans == "y" or ans == "":
          print()
          continue
        else:
          break
print('\nGoodbye.')
