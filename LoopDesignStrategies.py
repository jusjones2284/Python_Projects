import time
import random

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 5

startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
  number1 = random.randint(0,9)
  number2 = random.randint(0,9)

  if number1 < number2:
    number1, number2 = number2, number1

  answer = int(input("What is " + str(number1) + " - " + str(number2) + "? " ))

  if number1 - number2 == answer:
    print("You are correct! ")
    correctCount+= 1
  else:
    print("Your answer is wrong.\n", number1, "-" , number2, "should be", (number1 - number2))

  count += 1 

endTime = time.time()
testTime = int(endTime - startTime)

print("Correct count is", correctCount, "out of", 
      NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")

i = 1
while i < 10:
  if i % 2 == 0:
    print(i)
    i += 1 

while i < 10:
  if i % 2 == 0: 
    print(i)
  i += 1

data = input("Enter an integer (the input exits) " + "if the input is )" + 
             "if the input is 0: ")

data = int(input("Enter an integer (the input exits " + 
      "if the input is 0): "))
   
   
sum = 0
while data != 0:
    sum += data
   
    data = int(input("Enter an integer (the input exits " +
         "if the input is 0): "))

print("The sum is", sum)

number = int(input("Enter an integer: \
                \n or press 0 to exit"))
max = number

while number != 0:
    number = int(input("Enter an integer: "))
    if number > max:
      number = max
    
print("max is", max)
print("number", number)

      
