import random

# random_integer = random.randint(4, 10)
# random_float = random.random()
# print(random_integer)
# print(random_float)

intForCoin = random.randint(0,1)

# if (intForCoin == 0):
#   coin = "Heads"
# else:
#   coin = "Tails"

# print(coin)

# item1 = 1
# item2 = 2

# fruits = [item1, item2]
# fruits1 = ["Cherry", "Apple", "Pear"]
# fruits1.sort()
# print(fruits1)

# states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 
#  'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 
#  'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi',
#    'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 
#    'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 
#    'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 
#    'Hawaii']

# states.append("Justinland")
# states.extend("Spain", "Madrid")

# print(states[-1])
# names_string = input("enter random names ")

# names = names_string.split(", ")
# randomIndex = random.randint(0, len(names) - 1)
# randomName = names[randomIndex]
# print(randomName)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
veg = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirtyDozen = [fruits, veg]

print(dirtyDozen[1][1])


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number = position[1]
print(number)