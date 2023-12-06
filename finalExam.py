# import time
# print(2 ** 3)
# # print(x -= x + 4)
# print(int(time.time() / 1000000))

# print(ord('B'))

# print("Programming is fun"[-3:])

# s = "Chapter " + str(1)
# print(s)

# y = 0
# for i in range(0, 10, 2):
#   y += i
#   print("y = ", y, "i = ", i )

#   count = 0
#   while count < 10: 
#     print("helo world", count)
#     count += 1


# x = 0
# while x < 4:
#   x = x + 1

# print("x is", x)

# y = 0 
# for i in range(10, 1, -2):
#   y += i
# print(y)


# def fl(x = 1, y = 2): 
#   return x + y, x - y

# x, y = fl(y = 2, x =1)
# print(x, y)

# x1 = 1
# def f1():
#   x1 = 3
#   print(x1, end= " ")

# f1()
# print(x1)

# list1 = [0.5 * x for x in range(0, 4)]
# print(list1)

# list2 = [1, 3, 4]
# print(list2[-1])

# def f(i, values = []):
#   values.append(i)
#   return values
  

# f(1)
# f(2)
# v = f(3)
# print(v)

# myList = input("Enter numbers in a line: ").split()
# max= myList[0]
# indexOfMax = 0
# for i in range(1, len(myList)): 
#   if myList[i] > max: 
#     max = myList[i]
#     indexOfMax = i
# print(indexOfMax)

# # print(myList)

# d = {"john": 40, "peter": 45}

# print("john" in d)

# t = (1, 2, 4, 3)

# print(t[1:-1])

# print(set("abac"))


# n = int(input("Enter an integer number : "))

# largest_fact = 0

# if(n >= 2):
#   for j in range(1, n):
#     if n % j == 0:
#       largest_fact = j


# print("Largest Factor of {} is {}".format(n, largest_fact))


text = input("Enter a string: ").lower()
ltc = {}
for let in text:
    if let.isalpha():
        ltc[let] = ltc.get(let, 0) + 1
for let in sorted(ltc.keys()):
    if ltc[let] == 1:
        print("{} appears {} time".format(let, ltc[let]))
    else:
        print("{} appears {} times".format(let, ltc[let]))