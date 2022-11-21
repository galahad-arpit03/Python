print("Welcome to the tip calculator")

bill = input("What was the total bill ? ")
b = int(bill)

tip = input("What percentage tip would you like to give ? 10, 12, or 15 ? ")
t = int(tip)

total = b + (b*(t/100))

split = input ("How many people to split the bill ? ")
s = int(split)

print("Each will pay ",total/s," rs")