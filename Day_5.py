import random
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit) 
 


# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n]) 

# totalHeight = 0

# for height in student_heights:
#   totalHeight += student_heights
#   print(f"total heights  = {totalHeight}")


#   highest_score = 0
#   for score in student_scores:
#     if score > highest_score:
#       highest_score = score

# total = 0 

# for i in range(0, 101):
#   total += i

# print(total)

# target = int(input())
# even = 0 
# for i in range(0, target + 1, 2):
#   if target % i == 0:
#     even += 1
# print(even)

# target = 100
# for n in range(0, target + 1):
#   if (n % 3 == 0) and (n % 5 == 0): 
#     print("FizzBuzz")
#   elif (n % 3 == 0):
#     print("Fizz")
#   elif (n % 5 == 0):
#     print("Buzz")
#   else:
#     print(n)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! ")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How mnay numbers would you like?\n"))

# totalNumber = nr_letters + nr_numbers + nr_symbols
letters2 = []
for x in range(0, nr_letters):
  randomIndex = random.randint(0, len(letters) - 1)
  letters1 = letters[randomIndex]
  letters2.append(letters1)

for x in range(0, nr_symbols):
  numbers1 = random.randint(0, len(numbers) - 1)
  numbers2 = numbers[numbers1]
  letters2.append(numbers2)

for x in range(0, nr_numbers):
  numbers1 = random.randint(0, len(symbols) - 1)
  symbols1 = symbols[numbers1]
  letters2.append(symbols1)

random.shuffle(letters2)
print((letters2))

myList = ["apple", "banana", "cherry"]
random.shuffle(myList)
print(myList)

