# sum = 0
# for i in range(1, 11):
#   sum += i 
# print("Sum of integers from 1 to 10 is", sum)

# def sum(i1, i2):
#   result = 0
#   for i in range(i1, i2 + 1):
#     result += i 
#     return result
  

# def main():
#   print("Sum of integers from 1 to 10 is", sum(1, 10))
#   print("Sum of integers from 20 to 37 is", sum(20, 37))
#   print("Sum of integers from 35 to 49 is", sum(35,49))

# main()

# def convertPassword (original, specialChar): 
#   new = original.replace("a", "4")
#   new = new.replace("A", "4")
#   new = new.replace("e", "3")
#   new = new.replace("E", "3")
#   new = new.replace("I", "1")
#   new = new.replace("i", "1")
#   new = new.replace("o", "0")
#   new = new.replace("O", "0")
#   new = new.replace("u", "7")
#   new = new.replace("U", "7")

#   new = new + specialChar
#   return new

# userPwd = input("Please enter your desired password: ")
# userChar = input("Please enter your desired special character: ")

# newPwd = convertPassword(userPwd, userChar)
# print("Your new password is: " + newPwd)

# def max(num1, num2):
#   if num1 > num2: 
#     result = num1
#   else:
#     result = num2
  
#   return result
# x1 = 7
# x2 = 5
# print( max(x1, x2))


# return num1 if (num1 > num2) else num2
# total = 0

# def typing_speed(numOfWords, lengthOfTime):
#     if numOfWords > 0 and lengthOfTime > 0:
#         total = float (60  * numOfWords / lengthOfTime)
#         return total


# print(typing_speed(5, 1))

# def typing_speed(numberOfWordsPrsnTyped, lengthOfTimeintrvlInSec):
#     if numberOfWordsPrsnTyped >= 0 and lengthOfTimeintrvlInSec > 0:
#         typingSpeedInWrdsPrMint = float(60 * numberOfWordsPrsnTyped/lengthOfTimeintrvlInSec)
#         return typingSpeedInWrdsPrMint
    

# def typing_speed(words, interval):
#     mins = interval / 60
#     words_per_minute = words / mins
#     return words_per_minute
# speed1 = typing_speed(100, 100)
# print(speed1, "words per minute")
# speed2 = typing_speed(150, 100)
# print(speed2, "words per minute")

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
    
#     return True

def max(num1, num2):
    if(num1 > num2):
        result = num1
    else:
        result = num2

    return result

def main():
    i = 5
    j = 2
    k = max(i, j)
    print("The maxium between", i, "and", j, "is", k)

main()