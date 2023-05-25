total = float(input("What is the bill total?\n"))
print()

split = float(input("How many people are splitting the bill?\n"))
print()

tip = float(input("What percentage do you want to tip?\n"))
print()

TotalTip = float(total * (tip / 100))
TipRate = float((tip / 100) + 1)

share = (total * TipRate) / split

print(f"Each person should contribute ${share:.2f}. The total tip is ${TotalTip:.2f}.")
