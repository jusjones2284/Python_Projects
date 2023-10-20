# import re

# print("Enter an integer for seconds: ")
# seconds = int(input())
# minutes = seconds//60
# remainingSeconds = seconds % 60

# print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")

# from itertools import accumulate


# x1 = float(input("Enter the x-coordinate for point1: "))
# y1 = float(input("Enter the y-coordinate for point1: "))
# x2 = float(input("Enter the x-coordinate for point2: "))
# y2 = float(input("Enter the y-coordinate for point2: "))

# slope = (y2 - y1)/(x2 - x1)

# print("The slope for the line that connects two points" , (x1, y1), "and", (x2, y2), "is", slope)


# print("The slope for the line that connects two points ", (x1, y1) "and", (x2, y2), "is"  )

investmentAmount =float(input("Enter investment amount: ")) 
annualInterestRate = float(input("Enter anual interest rate: "))
numberOfYears = (float (input("Enter number of years: ")))
numberOfMonths = numberOfYears * 12
monthlyInterestRate = annualInterestRate/ 1200
futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

print("Accumulated value is", futureInvestmentAmount)

