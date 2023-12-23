print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? "))
party = int(input("How many people to split the bill? "))
tipPercentage = int(input("What percentage tip would you like to give? "))
totalTipPercentage = tipPercentage/ 100 
completeTotal = totalBill + (totalBill * totalTipPercentage)
perPersonCost = completeTotal/party
print("Each person should pay: ", "$",perPersonCost)

print(6 + 4/2 - (1 * 2))

name = input("What is your name?")
print(f"hello, {name}")

age = 12
print(f"You are {age} years old")