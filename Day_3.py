# print("Welcome to Treasure Island")
# print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")
# answer1 = input().lower()
# if answer1 == "right":
#   exit
# else:
#   print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross") 
#   answer2 = input().lower()
#   if answer2 == "swim":
#     exit
#   else: 
#     print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
#     houseColor = input().lower()
#     if houseColor == "red": 
#       print("it's a full of fire Game over")
#     elif houseColor ==  "yellow":
#       print("room full of mustard maybe game over")
#     elif houseColor == "blue":
#       print("you win")


# print("Thank you for choosing Python Pizza Deliveries!")
# size= input("What size pizza do you want? S, M, or L ").upper()
# add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N ").upper()

# bill = 0

# if size == 'S':
#   bill += 15
# elif size == 'M':
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == 'Y':
#   if size == 'S':
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == 'Y':
#   bill += 10

# print(f"Your final bill is {bill}")

# if size == 'S' and add_pepperoni == 'Y':
#   bill += 10
# elif size == 'M' and add_pepperoni == 'Y':
#   bill += 15

# height = 90

# if height >= 120:
#   print("You can ride the rollercoaster! ")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5. ")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7. ")
#   elif age >= 45 and age <= 55: 
#     print("everything is going to be ok. have a ride on the roller coaster")
#   else:
#     bill = 12
#     print("Adult tickets are $12")


print("What is your name? ")
firstPerson = input().lower()
print("What is their name? ")
secondPerson = input().lower()

combineNames = firstPerson + " " + secondPerson
t = combineNames.count('t')
r = combineNames.count('r')
u = combineNames.count('u')
e = combineNames.count('e')
first_digit = t + r + u + e 

l = combineNames.count('l')
o = combineNames.count('o')
v = combineNames.count('v')
e = combineNames.count('e')
secondDigit = l + o + v + e 

score =  int(str(first_digit))+ int(str(secondDigit))


if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos. ")
elif (score >= 40) and (score <= 50):
  print(f"your score is {score}, you alright together")
else:
  print(f"Your score is {score}")

# print(firstPerson.count("j"))