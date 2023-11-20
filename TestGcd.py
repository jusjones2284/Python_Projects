import random
# from GCDFunction import gcd

# n1 = int(input("Enter the first integer: "))
# n2 = int(input("Enter the second integer: "))

# print("The greatest common divisor for", n1, "and", n2, "is",\
#       gcd(n1, n2)
#       )

# def isPrime(number):
#   divisor = 2
#   while divisor <= number/2:
#     if number % divisor == 0:
#       return False
#     divisor += 1
#   return True

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()
# print("Python is " , x)

# y = 1
# def increase():
#   global y
#   y += 5

# increase()
# print(y)

# def f(x, y = 1, z = 2):
#   return x + y + z 

# print(f(x = 9))
# print(f(7))
# print(f(0, 2, 100))

# def printArea(width = 1, height = 2):
#   area = width * height 
#   print("width:", width, "\theight:", height, "\tarea:", area)

# printArea()
# printArea(4, 2.5)

# def j(w = 1, h = 2):
#   print(w, h)

# f()

# def sort(number1, number2):
#   if number1 < number2:
#     return number1, number2
#   else: 
#     return number2, number1
  
# n1, n2 = sort(3, 2)
# print("n1 is", n1)
# print("n2 is", n2)

# def t(x, y):
#   return x + y, x - y, x * y, x / y

# t1, t2, t3, t4 = t(9,5)
# print(t3, t4)

# random.randint()

jus = random.randint(34, 55)
random.randint(ord('a'), ord('z'))


def binaryToHex(binaryValue):
   
    decimal_value = int(binaryValue, 2)
    hex_value = hex(decimal_value).upper()
    hex_value = hex_value[2:]

    return hex_value

if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    try:
        int(binary_input, 2)
        hex_result = binaryToHex(binary_input)
        print("The hex value is", hex_result)
    except ValueError:
        print("Invalid binary input. Please enter a valid binary number.")


def convertMillis(millis):
    millis = millis // 1000
    h = millis//3600
    millis = millis % 3600
    m = millis // 60
    millis = millis % 60
    s = millis
    return ""+str(h)+":"+str(m)+":"+str(s)


def main():
    millis = int(input("Enter time in milliseconds: "))
    print(convertMillis(millis))

main()

def count(s, ch):
    count = 0
    for character in s:
        if character == ch:
            count += 1
    return count

if __name__ == "__main__":
    user_string = input("Enter a string: ")
    user_char = input("Enter a character to count: ")
    if len(user_char) != 1:
        print("Please enter a single character.")
    else:
        occurrences = count(user_string, user_char)
        print(f"The character '{user_char}' occurs {occurrences} times in the string.")


def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    futureValue = investmentAmount * (1 + monthlyInterestRate) ** (years * 12)
    return futureValue

investmentAmount = int(input("The amount invested: "))
annualInterestRate = float(input("Annual interest rate: "))


monthlyInterestRate = annualInterestRate/12/100

print()
print("{:<5} {:>15}".format("Year", "Future Value"))

for year in range(1,31):
    futureValue = futureInvestmentValue(investmentAmount,monthlyInterestRate,year)
    print("{:<5} {:>15.2f}".format(year, futureValue))





def calculate_series(i):
    ans = 0.0

    for j in range(0, i + 1):
        ans = ans + (float)(0 + j)/(1 + j)
    return ans

def main():
    print("i  m(i)")
    for i in range(1, 21):
        print(str(i) + "  " + format(calculate_series(i), '.4f'))

if __name__ == "__main__":
    main()

