import random

# count = 0
# while count < 10:
#   print("Programming is fun")
#   count += 1

# if count < 1:
#   print("hello world")

# counts = 0 
# while counts < 30: 
#   if counts <= 10:
#     print("count is less than 10 ", counts)
#     counts += 1
#   if counts <= 20:
#     print("count less than 20", counts)
#     counts += 1

# numbers = 0 
# while numbers < 100: 
#   print("Programming is fun! ")
#   numbers += 1

# sum = 0
# i = 0 
# while i < 10: 
#   sum = sum + i
#   i = i + 1
# print("sum is", sum)

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
  number1, number2 = number2, number1

cA = number1 - number2

answer = int(input("what is " + str(number1) + 
                   " - " + str(number2) + "? "))
if(cA == answer):
  print("You got it!")
else:
  print("Game over")

