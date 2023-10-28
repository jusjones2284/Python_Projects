import random
import turtle
lottery = random.randint(0, 99)

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

turtle.pendown() # Pull the pen up
