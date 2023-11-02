import random
import turtle
lottery = random.randint(0, 99)
import math

# guess = int(input("Enter your lottery pick (two digits): "))

# lotteryDigit1 = lottery // 10
# lotteryDigit2 = lottery % 10

# guessDigit1 =  guess // 10
# guessDigit2 = guess % 10

# print("The lottery number is", lottery)

# if guess == lottery: 
#   print("Exact match: you win $10,000")
# elif (guessDigit2 == lotteryDigit1 and \
#         guessDigit1 == lotteryDigit2
#         ):
#   print("Match all digits: you win $3,000")
# elif (guessDigit1 == lotteryDigit1
#         or guessDigit1 == lotteryDigit2
#         or guessDigit2 == lotteryDigit1
#         or guessDigit2 == lotteryDigit2):
#   print("Match one digit: you win 1,000")
# else: 
#   print("Sorry, no match")

# ch = 'a'

# print(ch >= 'A' and ch >= 'Z')

# print(ch >= 'A' and ch <= 'Z')

# print('A' <= ch <= 'Z')

# print(ch >= 'A' or ch <= 'Z')

# # x = 14
# # y = 15

# # print(x % 2 == 0 and y % 2 == 0)
# # print(x % 2 != 0 and y % 2 != 0)
# # print(x % 2 == 0 or y % 2 == 0)
# # print(x % 2 == 0 and y % 2 == 1)


# # x > y or x < y
# # x >= y or x <= y
# # not (x == y)
# # x > y and x < y

# # if x > 0: 
# #   y = 1
# # else:
# #   y = -1

# # number1 = 4
# # number2 = 8
# # max = number1 if number1 > number2 else number2

# # print("number is even" if number2  % 2 == 0 else "number is odd")
# # n1 = 5
# # n2 = 3
# # status = 1 if n1 > n2 else (0 if n1 == n2 else -1)

# # x = float(input("Enter a number: "))
# # y = float(input("Enter a number: "))  
# # z = float(input("Enter a number: "))
# # print("sorted" if x < y and y < z else "not sorted")

# ages = 5
# ticketPrice = 20 if (ages >= 16) else 10
# print(ticketPrice)

# age = 9
# ticketPrices = 40 if age >= 7 else 87

# count = 9
# print(count, end = "*" if count % 10 == 0 else "#")  

# scale = 8
# x = 6
# score = 3 * scale if x > 10 else 4 * scale

# if x > 10:
#   score = 3 * scale 
# else:
#   score= 4 * scale

# income = 100
# tax = income * 2.0 if income > 100000 else income * 4.0 + 1000

# income * 0.2 if income > 198837 else 0.1

# number = 2

# even = True if number % 2 == 0 else False
# print(even)

# year = int (input("Enter a year: "))
# match year % 12:
#   case 0: print("monkey")
#   case 1: print("rooster")

# x = 1
# a = 3

# if a == 1:
#   x += 5
# elif a == 2:
#   x += 10
# elif a == 3:
#   x += 16 

# match a:
#   case 1: x += 5
#   case 2: x += 10
#   case 3: x += 8

# day = 9
# match day:
#   case 0: print("Sunday")

# month = "Dec"

# match month:
#   case "jan": print("january")
#   case "Dec": print("dec 22")
#   case "march": print("someone else")

# turtle.pendown() # Pull the pen up

# minutes = int(input("Enter the number of minutes: "))
# totalNumberOfDays = minutes // (24 * 60)
# numberOfYears = totalNumberOfDays // 365
# remainingNumberOfDays = totalNumberOfDays % 365
# print(minutes, "minutes is approximately", numberOfYears, "years and", remainingNumberOfDays, "days")

# print('Find roots of the quadratic equation: ax^2 + bx + c = 0')

# a = float(input('Enter a value of a: '))
# b = float(input('Enter a value of b: '))
# c = float(input('Enter a value of c: '))

# discriminant = b ** 2 - 4 * a * c

# if discriminant > 0:
#   r1 = (-b + discriminant ** 0.5)/(2 * a)
#   r2 = (-b - discriminant ** 0.5)/(2 * a)
#   print('Roots are', r1, 'and', r2)

# elif discriminant == 0:
#   r = -b/(2*a)
#   print('Root is', r)

# else:
#     print('The equation has no real roots.')

  
 
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))
# d = float(input("Enter the value of d: "))
# e = float(input("Enter the value of e: "))
# f = float(input("Enter the value of f: "))

# determinant = a * d - b * c

# if determinant == 0:
#     print("The equation has no solution.")
# else:
#     x = (e * d - b * f) / determinant
#     y = (a * f - e * c) / determinant

#     print("Solution:")
#     print("x =", x)
#     print("y =", y)

#     def calculate_day_of_week(year, month, day):
#     if month == 1 or month == 2:
#         month += 12
#         year -= 1
    
#     q = day
#     m = month
#     j = year // 100
#     k = year % 100
#     # Apply Zeller's congruence formula
#     h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
#     # Map the result to the corresponding day of the week
#     days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#     day_of_week = days_of_week[h]
    
#     return day_of_week
# # Get input from the user
# year = int(input("Enter year: (e.g., 2012): "))
# month = int(input("Enter month: 1-12: "))
# day = int(input("Enter the day of the month: 1-31: "))
# # Calculate and print the day of the week
# day_of_week = calculate_day_of_week(year, month, day)
# print("Day of the week is", day_of_week)

# month = int(input("Enter a month in the year (e.g., 1 for Jan): "))
# year = int(input("Enter a year: " ))

# isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# if isLeapYear == False:
#         days = 28
# else:
#         days = 30

# # match month:
# #    case 1: month = "Jan"  print(month, year, "has", days)
# #    case 2: month = "feb"
      
# match month:
#         case 1: "January" , year , "has 31 days"
#         case 2: "February", year , "has", 
# x = 2
x = -2.5
print(abs(x))
x1, x2 = 4, 5
print(max(x1, x2))
print(min(x1, x, x2))
pow(2, 4)
round(x)
round(x, x1)

print(math.degrees(math.pi/2))

letter = 'A'
numChar = '4'
message = "Good morning"
x =''

print('''There are three ways to represent strings: 
      1. Single-quotes
      2. Double-quotes, and
      3. Tripple-quotes.
''')

s1 = "Welcome"
print("come" in s1)

"come" not in s1

"Welco" in s1
"Welco" not in s1 is False

"green" == "glow"
"green" != "glow"

""
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if (s1 > s2):
  s1, s2 = s2, s1

print("The two strings are in this order: ", s1, s2)

s = "Welcome"
len(s)


