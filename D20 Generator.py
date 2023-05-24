# D20 Generator
import random

print(random.randint(0, 21))
while True:
    print("Again?")
    Ans = input()
    if Ans == "Y":
        print()
        print(random.randint(1, 20))
    elif Ans == "y":
        print()
        print(random.randint(1, 20))
    elif Ans == "yes":
        print()
        print(random.randint(1, 20))
    elif Ans == "Yes":
        print()
        print(random.randint(1, 20))
    elif Ans == "":
        print()
        print(random.randint(1, 20))
    else:
        break
print()
print("Goodbye.")
