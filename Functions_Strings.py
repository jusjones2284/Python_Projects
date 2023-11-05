# s = "Welcome"
# len(s)
# print(len(s))

# s = input("Enter a string: ")

# if len(s) % 2 == 0:
#   print(s, "contains an even number of characters")
# else:
#   print(s, "contains an odd number of characters")


# s1 = "Welcome to python"
# s2 = "to"
# len(s1)

# print(max("Programming is fun"))
# print(s1[0])
# print(s1[-1])
# sliced = s1[0:3]
# print(sliced )

# s1[1:-1]

# response = (input("Do you want to continue(Enter yes or no)")).lower()
# # response = response.lower()

# if response == "yes":
#   print("Continuing...")
# elif response == "no":
#   print("Exiting...")
# else:
#   print("invaild response")

# S = input("Enter a String: ")
# if S.isdigit():
#   print(S, "is a numberic string")
# else:
#     print("isnt a numberic string")

s = "welcome to python"
print(s.endswith("thon"))
s.startswith("djka")
s.find("come")
s.rfind("become")
s.count("o")

n = input("Enter a string: ")
if n.startswith("comp"):
  print(n, "begins with")
if n.endswith("er"):
  print(n, "ends with er")

count = n.count('e')
print('e', "appears", count, "times" if count > 8 else "time", "in", n)

s = input("Enter a string with length > 1")
lastCh = s[-1]
if s[:-1].find(lastCh):
  print(lastCh, "appears more than once in", s)
else:
  print(lastCh, "appears only once in", s)

"Good".replace("o", "9")

n = "   Welcome to Python\t"
n1 = n.lstrip() ##left strip
n2 = n.rstrip() ##right strip
n4 = n.strip()  ##complete strip


