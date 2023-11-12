# n1 = int(input("Enter first integer: "))
# n2 = int(input("Enter second integer: "))

# gcd = 1
# k = 2
# while k <= n1 and k <= n2:
#   if n1 % k == 0 and n2 % k == 0:
#     gcd = k
#   k += 1
# print("The greatest common divisor for", 
#       n1, "and", n2, "is", gcd)


for i in range(10):
  for j in range(10):
    print(i * j)


if n == 2:
  is_prime = True
elif n%2 == 0:
  is_prime = False
else:
  is_prime = True
  for m in range(3, int(n**0.5)*1,2):
    if n% m == 0:
      is_prime = False

d = int(input("Enter the distance (common difference): "))
n = int(input("Enter the integer number n: "))
sum = 0
num = 1

while num <= n:   
    sum = sum + num 
    num = num + d
print("The sum of elements of arithmetic progression:", sum)


while num < 20:
  num += 1
  sum += num
  if sum >= 100: 
    break
print("The number is", num)
print("The sum is")

while num < 20:
  num += 1
  if num == 10 or num == 11:
    continue
  sum += num
print("The sum is", sum)

n = int(input("Enter an integer >= 2: "))
factor = 2

while factor <= n:
  if n % factor == 0:
    break
  factor += 1
print("The smallest factor other than 1 for", n, "is", factor)

factor =2
while factor <= n and n % factor != 0:
  factor += 1


