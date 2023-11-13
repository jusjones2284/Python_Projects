s = input("Enter a string: ")

low = 0

high = len(s) -1
print(s[high])

isPalindrome = True
while low < high:
  if s[low] != s[high]:
    isPalindrome = False
    break

  low += 1
  high -= 1

if isPalindrome:
  print(s, "is a palindrome")
else:
  print(s, "is not a palindrome")

  for i in range(len(s1)):
    s3 += s1[i] + s2[i]


s3 = ""
for i in range(min(len(s1), len(s2))) :
  s3 += s1[i] + s2[i]


s1 = 'hello'
s2 = 'world'
length = len(s1)
s3 = ''
for i in range(len(s1)):
    s3 += s1[i] + s2[i]
print(s3)

s1 = 'hello'
s2 = 'world'
length = len(s1)
s3 = ''
for i in range(len(s1)):
    s3 += s1[i] + s2[i]

s3 = ""
for i in range(max(len(s1), len(s2))) :
    if i < len(s1) : s3 += s1[i]
    if i < len(s2) : s3 += s2[i]

s3 = ""
for i in range(min(len(s1), len(s2))) :
  s3 += s1[i] + s2[i]



positive_count = 0
negative_count = 0
total = 0
count = 0

while True:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    
    if num == 0:
        break
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    
    total += num
    count += 1

if count > 0:
  
    average = total / count
    
    print(f"The number of positives is {positive_count}")
    print(f"The number of negatives is {negative_count}")
    print(f"The total is {total}")
    print(f"The average is {average:.2f}")
else:
    print("You didn't enter any number")



students = []


num_students = int(input("Enter the number of students: "))


for _ in range(num_students):
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))
   
    students.append((name, score))

students.sort(key=lambda x: x[1], reverse=True)

print("\nTop two students:")
print(f"{students[0][0]}'s score is {students[0][1]}")
print(f"{students[1][0]}'s score is {students[1][1]}")


str=input("Enter a string: ")
vowels = 0
consonant = 0
for i in range(0, len(str)):
  ch = str[i]
if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):

  ch=ch.lower()

if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
  vowels += 1
else:
  consonant += 1

print("The number of vowels is ", vowels)
print("The number of consonants is", consonant)



VOWELS = 'aeiou'
CONSONTANTS = 'bcdfghjklmnpqrstvwxyz'

vowel_count = 0
consonant_count = 0

string = input('Enter a string: ').lower()

for letter in string:
 
    if letter in VOWELS:
        vowel_count += 1
   
    elif letter in CONSONTANTS:
        consonant_count += 1

print('The number of vowels is', vowel_count)
print('The number of consonants is', consonant_count)


def calculate_isbn13_checksum(digits):
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += int(digits[i])
        else:
            total += 3 * int(digits[i])
    
    checksum = 10 - total % 10
    if checksum == 10:
        checksum = 0
    return checksum

def main():
    input_str = input("Enter the first 12 digits of an ISBN-13 as a string: ")
    
    if len(input_str) != 12 or not input_str.isdigit():
        print("Incorrect input")
        return
    
    checksum = calculate_isbn13_checksum(input_str)
    
    isbn13 = input_str + str(checksum)
    
    print("The ISBN-13 number is", isbn13)

if __name__ == "__main__":
    main()