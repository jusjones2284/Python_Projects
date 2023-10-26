import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
  number1, number2 = number2, number1

answer = int(input("What is " + str(number1) + "-" + str(number2) + "? "))

if number1 - number2 == answer:
  print("youre correct")

else: print(number1, '-', number2, "is", number1 - number2)

pay = 100

score = 8
if score > 90: 
  pay *= 1.03
else: pay *= 1.01

x = 2
y = 2
if x > 2:
  if y > 2:
    z = x + y
    print("z is " + z)

age = 1

if age < 16: 
  print("Cannot get a drivers license")
if age >= 16:
  print("Cannot get a driver's license")

if number1 % 10 == 0:
  print("Hi five")
elif number2 % 20 == 0:
  print("heck no")

if