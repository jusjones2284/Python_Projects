import math
# # day = 0
# # question1 = "Is your birthday in Set1?\n " + \
# #     "1 3 5 7\n" + \
# #     "9 11 13 14\n" + \
# #     "17 19 21 23\n" +\
# #     "\nEnter n/N for No and y/Y for yes:"
    
# # answer = input(question1)

# # if answer.upper() == "Y":
# #     day += 1

# # question2 = "\nIs your birthday in Set2?\n" + \
# #     "2 3 6 7\n" + \
# #     "10 11 14 15\n" + \
# #     "18 19 22 23\n" + \
# #         "\nEnter n/N for No and y/Y for Yes:"
        
# # answer = input(question2)

# # if answer.upper() == "Y":
# #     day += 5

# # print("\nYour birthday is " + str(day) + "!")

# # amount = 12618.98
# # interestRate = 0.0013
# # interest = amount * interestRate
# # print("Interest is", interest) 
# # print("Interest is", round(interest, 2) )
# # print("Interest is", format(interest, ".2f"))

# # print(format(57.467657, "10.2f"))
# # print(format(123456782.923, "10.2f"))

# # print(format(57.4747478, "10.2e"))
# # print(format(45.48032, "10e"))
# # print(format(48584.49499, "10.2%"))
# # print(format(4328492.94302, "10.2%"))

# # print(format(57.46757, "<10.2f"), end='*')

# # print(format("Welcome to Python", "20s"))
# # print(format("Welcome to Python", "<20s"))

# from math import degrees
# import math


# weight = 140
# height = 73
# Degrees = 38
# Radians = 90
# Sine = 32
# Cosine = 33
# Tangent = 8

# # f{"Weigth is {weight} and {height}"}

# print(f"{'Degrees':<10s} {'Radians':<10s}",
#     f"{'Sine':<10s} {'Cosine':<10s}", 
#     f"{'Tangent':<10s}")

# print(format(45, "5d"))
# print(format(45, "<5d"))


#Prompt the user to enter the numberOfSides (int) and the lengthOfSide (float) of a polygon, and apply the formula to compute the area of the polygon.

# n = float(input("Enter the Number of Sides: "))
# s = float(input("Enter the side: "))


# area = (n * pow(s, 2)) / (4 * math.tan(math.pi / 6))

# print("The area of the polygon is:", area)


# n = int(input("Enter the number of sides: "))
# side = float(input("Enter the side: "))
# area = (n * pow(side, 2) )/ math.tan(math.pi / n) / 4
# print("The area of the polygon is", area)

# grade = input("Enter a letter grade: ")

# if grade.upper == 'A':
#     print('The numberic value for grade', grade, 'is', 4)

# value = 0
# for i in range(10):
#   value += 5
#   print(value , ", ", i)


# ##firs number is the start value. second number is the the end and the last is the iteration by.
# for i in range(5, 55, 5):
#   print(i)

# for i in range(5, 100, 5):
#   print(i)

# for v in range(4, 8):
#   print(v)

# number = 0
# sum = 0

# for count in range(5):
#   number = int(input("Enter an integer: "))
#   sum += number

# print("sum is", sum)
# print("count is", count)

# count = 0
# sum = 0

# for count in range(5, 10):
#   number = int(input("Enter an integer: "))
#   sum = sum + number

# print("sum is", sum)
# print("count is", count)

# sum = 0
# i = 0
# while i <= 1001: 
#   sum += i
#   i += 1

# for i in range(0, 1001):
#   sum += i 

for i in range(1,5):
  j = 0
  while j < i :
    print(j, end= " ")
    j += 1

sum = 0

i = 0.01
while i <= 1.0:
  sum += i 
  i = i + 0.01
print("the sum is", sum)


count = 0 
i = 0.01
while count < 100:
  sum += i 
  i = i + 0.01
  count += 1
print("The sum is", sum)

for count in range(100):
  sum += i 
  i = i + 0.01

print("The sum is", sum)