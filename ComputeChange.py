# import time
# import turtle as turtle
# turtle.title("1st turtle")
# amount = float(input("Enter the amount, for example, 11.56: "  ))

# remainingAmount = int(amount * 100)

# numberOfDollars = remainingAmount // 100
# remainingAmount = remainingAmount % 100

# numberOfQuarters = remainingAmount // 25
# remainingAmount = remainingAmount % 25

# numberOfDimes = remainingAmount // 10
# remainingAmount = remainingAmount % 10

# numberOfNickles = remainingAmount // 5
# remainingAmount = remainingAmount % 5

# numberOfPennies = remainingAmount

# print(10.03 * 100)
# r =0
# t =0
# 5.5 * (r + 2.5)** (2.5 + t)

# count = 0
# count = count + 1

# from multiprocessing.sharedctypes import Value
# from tokenize import Double
# import turtle


# # value = 5
# # print(double(value))

# # value = 5.7
# # print(int(value))
# # print(round(value))
# ct = time.time()
# totalSeconds = int(ct)
# seconds = totalSeconds * 60
# print()

# annualInterestRate = float (input ("Enter annual interest rate: "))
# monthlyInterestRate = annualInterestRate/1200 

# numberOfYears  = int(input("Enter number of years: ")) 
# totalNumberOfMonths = numberOfYears / 12

# loanAmount = float(input("Enter loan amount: ")) 

# monthlyPayment = (loanAmount * monthlyInterestRate )* totalNumberOfMonths

# print(monthlyPayment)

# x1 = float(input("Enter x-coordinate for Point 1: ")) 
# y1 = float(input("Enter y-coordinate for Point 1: ")) 
# x2 = float(input("Enter x-coordinate for Point 2: ")) 
# y2 = float(input("Enter y-coordinate for Point 2: "))

# x1 = float(input("Enter x-coordinate for Point 1: "))
# y1 = float(input("Enter y-coordinate for Point 1: "))
# x2 = float(input("Enter x-coordinate for Point 2: "))
# y2 = float(input("Enter y-coordinate for Point 2: "))
              
# # Compute the distance
# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# # Display two points and the connecting line
# turtle.penup()
# turtle.goto(x1, y1) # Move to (x1, y1)
# turtle.pendown()
# turtle.write("Point 1", font=("Times", 12)) 
# turtle.goto(x2, y2) # draw a line to (x2, y2)
# turtle.write("Point 2", font=("Times", 12))

# # Move to the center point of the line
# turtle.penup()
# turtle.goto((x1 + x2) / 2, (y1 + y2) / 2) 
# turtle.write(distance, font=("Times", 12))

# turtle.done() 

# print((4.5 + -5.5) + (6.6 + -6.5))

if radius < 0: 
  print("Incorrect input")
else: 
  area = radius * radius * 3.14159
  print("Area is", area)