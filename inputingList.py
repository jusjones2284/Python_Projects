import random
import statistics

# list1 = []
# print("Enter 10 numbers, one number per line")
# for i in range(10):
#   list1.append(float(input()))

# list2 = []
# print("Enter 5 numbers, one per line")
# for i in range(5):
#   list2.append(float(input()))

# s = input("Enter 10 numbers separeted by spaces on one line: ")
# items = s.split()
# list4 = [float(x) for x in items]
# print(list4)

# j = input("Enter a string for numbers: ")
# item = j.split()
# [float(x) for x in item]

# lst = [4, 5, 6, 7, 8,9]
# temp = lst[0]

# for i in range(1, len(lst)):
#   lst[i - 1] = lst[i]
# print(lst)
# lst[len(lst) - 1] = temp

# lst = lst[1: len(lst)] + lst[0:1]
# lst = lst[len(lst) // 2 : len(lst)] + lst[0 : len(lst) // 2]

# myList = [1,2,3,4,5,6]

# for i in range(1,6):
#   myList[i - 1] = myList[i]
# for i in range(0, 6):
#   print(myList[i], end = " ")

# months = ["January", "February", "March", "April", 
#             "May", "June", "July", "August", "September",
#               "October", "November", "December"]
  
# month = int(input("Enter a month number(1 to 12): "))

# print("the month is ", months[month - 1])

# lst = 100 * [False]
# print(lst)
# lst.append(5.5)
# print(lst[3] + lst[6])
# total = sum(lst[0:5])
# print(list[random.randint(0, len(lst) - 1)])

list1 = [1,2,3,4]
print(statistics.mean(list1))

list2 = [1,8,7,3,2]
print(statistics.median(list2))

list5 = [1, 7, 1, 3, 2]
statistics.mode(list5)

##average 
statistics.mean(list5)
##middle value
statistics.median(list5)
##most common value
statistics.mode(list5)

NUMBER_OF_ELEMENTS = 3
numbers = []
sum = 0

for i in range(NUMBER_OF_ELEMENTS): 
  value = int(input("Enter a number: "))
  numbers.append(value)
  sum += value

average = sum / NUMBER_OF_ELEMENTS

count = 0
for i in range(NUMBER_OF_ELEMENTS):
  if numbers[i] > average:
    count += 1
# for i in range(NUMBER_OF_ELEMENTS):
#   if numbers[i] > average:
#     count += 1

print("Average is", average)
print("Number of elements above the average is", count)

cards = 52

deck = [x for x in range(cards)]

decks= len(cards)

list2 = [x for x in list1]

list = [1, 43]
list2 = [x for x in list]