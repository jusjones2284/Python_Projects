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

studentsGrade = int(input("what is your grade? "))

if score >= 90.0:
  print("grade is A")
  if score >= 80.0:
    print("grade is B")
    if score >= 70.0:
      print("grade is C")
      if score >= 60.0:
        print("grade is D")
      else: 
        print("grade is F")



year = int(input("Enter a year: "))

zodiacYear = year % 12

if zodiacYear == 0:
  print("monkey")
elif zodiacYear == 1: 
  print("rooster")
elif zodiacYear == 2:
  print("dog")
elif zodiacYear == 3:
  print("pig")
else: 
  print("sheep")

i = 1
j = 2
k = 3

if i > j: 
  if i > k: 
    print("Hello world")
  else:
    print("good bye")

  
  even = number1 % 2 == 0

count = 8
words = "hello"

if words == "hello":
  print("you got it right")

if count % 10 == 0:
  newLine = True 

newLine = count % 10 == 0


if x > 2:
  if y > 2:
    z = x + y
else: 
  print("x is", x)

weight = float(int(input("Enter weight in pounds: ")))

height = float (input("Enter height inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weight * KILOGRAMS_PER_POUND

heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms/ (heightInMeters * heightInMeters)

number = int(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
  print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
  print(number, "is divisble by 2 or 3")

if(number % 2 == 0 or number % 3 == 0) and \
  not (number % 2 == 0 and number % 3 == 0): 
  print(number, "is divisible by 2 or 3, but not both ")

  ##chain operators 
  0 <= x <= 1
num = 9
(x > 1) and (x < 100)
(num > 1) and (num < 100)
(num > 5) and (num < 200) or (num < 0)

(x > 1) and (x < 100)
(x > 1) and (x < 100) or (x < 0)

(-4.5 < x - 5 < 4.5)
50 <= x <= 100

x = float(input("Enter a number: "))
y = float(input("Enater a number: "))
z = float(input("Enter a  number: "))

(x > 13) and (x < 18)

weight > 50 or height > 160

weight > 50 and height > 160

(weight > 50 or height > 160) and not (weight > 50 and height > 160)

