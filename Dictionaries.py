# empList = ["Jones", "Garcia", "Wang", "Jones", "Alda"]
# print(type(empList))


# #set 
# empSet = {5, 10, 38}
# filledSet = set((20,25,89))
# print(type(filledSet))

# #tuple
# myTuple = ("apple", "bannana", "cherry")
# print(type(tuple(filledSet)))

# #dictionary
# empDict = {3214: "Jones", 8743: "Garcia", 3343: "Wang", 
#            4437: "Jones", 5467: "Alda"}
# print(empDict[3214])
# empDict[1111] = "NewEmp"
# print(empDict)
# empDict[1111] = "newJones"
# print(empDict)

# students = {"111-34-3434": "Ashley", "132-56-6290": "Gabriel"}

# d = {}
# d = dict()

# j = {1:[1,3], 3:[4,5]}
# jk = {(1,2):1, (4,2):2}
# jkl = {1: "Ashley", 3: "beth"}
# jklm = {}

# print(empDict.get(874))
# print(len(empDict))

# print(empDict)
# del empDict[1111]
# print(empDict)
# # del empDict["Jones"]

# students1 = {"111-34-3434":"Ashley", "132-56-6290": "Gabriel"}
# for key in students1: 
#   print(key + ":" + str(students1[key]))


# def main():
#   d = {}
#   d["helena"] = 50
#   d["bakary"] = 45
#   d["aiysha"] = 54
#   d["helena"] = 51
#   d["ashley"] = 53

# students = {"111-34-3434":"Ashley", "132-56-6290":"Gabriel"}
# "111-34-3434" in students
# "111-34-3434" not in students

# not_found = set()

# for key in lst:
#     if key in d:
#         del d[key]
#     else:
#         not_found.add(key)

# d1 = {"red": 41, "blue": 3}
# d2 = {"blue": 3, "red":41}
# d1 == d2

# d6 = {"john":40, "peter":45}
# d7 = {"john":466, "peter":45}
# print(d6 > d7)

students = {"111-34-3434": "Ashley", "132-56-6290": "Gabriel"}
print(tuple(students.values()))
print(students.keys())

tuple(students.items())

students.get()

students5 = {"ashley":3, "gabriel": 2}
len(students5)
students5.keys()
students5.values()
students5.items()

party_size = {}
for key in mp_affiliation :
  if mp_affiliation[key] in party_size :
    party_size[mp_affiliation[key]] += 1
  else :
    party_size[mp_affiliation[key]] = 1


  d3 = {}
for a,b in d1.items() :
  if a not in d2:
    d3[a] = d1[a]
for a,b in d2.items() :
  if a not in d1:
    d3[a] = d2[a]

d3 = {}


for a, b in d1.items():   
    if b in d2:
        c = d2[b]
        d3[a] = c

d3 = {}
for a,b in d1.items() :
  if b in d2.keys() :
    d3[a] = d2[b]

inverse = {}
for key in d.keys() :
  val = d[key]
  inverse[val] = key

  winner = None
for key, votes in election_results.items() :
  if winner == None or votes > max :
    max = votes
    winner = key

squares = dict([(i, i*i) for i in range(1, n+1)])


import keyword
keywords = keyword.kwlist
count = {}
source_code = input("Enter Python source code: ")
words = source_code.split()
for word in words:
    if word in keywords:
        if word not in count.keys():
            count[word] = 1
        else:
            count[word] = count[word]+1
final_keywords = list(count.keys())
final_keywords.sort()
for keyword in final_keywords:
    print("{}: {}".format(keyword,count[keyword]))

def main():
    input_text = input("Enter a text: ")
    words = input_text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    non_duplicate_words = [word for word, count in word_count.items() if count == 1]
    
    non_duplicate_words.sort()
    
    result = ' '.join(non_duplicate_words)
    print(result)

if __name__ == "__main__":
    main()


def display_nonduplicate_words(text):
    words = text.split()

    unique_words = set()

    for word in words:
        unique_words.add(word)

    sorted_words = sorted(list(unique_words))

    result = " ".join(sorted_words)
    print(result)


    def main():
    input_text = input("Enter a text: ")
    words = input_text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    non_duplicate_words = [word for word, count in word_count.items() if count == 1]
    
    non_duplicate_words.sort()
    
    result = ' '.join(non_duplicate_words)
    print(result)

if __name__ == "__main__":
    main()





text = input("Enter a text: ")
vowels, consonants = 0, 0
for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("The number of vowels is {} and consonants is {}".format(vowels, consonants))

modelYear = 2000  

norecall = not (1995 <= modelYear <= 1998 or 2004 <= modelYear <= 2006)


modelYear = 2000  

norecall = not (1995 <= modelYear <= 1998) and not (2004 <= modelYear <= 2006)

print(norecall)

modelYear = 2000  

norecall = not (1995 <= modelYear <= 1998 or 2004 <= modelYear <= 2006)


def calculate_day_of_week(year, month, day):
    
    if month == 1 or month == 2:
        month += 12
        year -= 1

   
    j = year // 100
    k = year % 100
    h = (day + 26 * (month + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7


    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    return days_of_week[h]


Certainly! Here's the Python program implementing Zeller's congruence to calculate the day of the week:

python
Copy code
def calculate_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1

    j = year // 100
    k = year % 100
    h = (day + 26 * (month + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    return days_of_week[h]


y = int(input("Enter year: (e.g., 2008): "))

m = int(input("Enter month: 1-12: "))
if m==1:
    m=13
    y=y-1
elif m==2:
    m=14
    y=y-1

q = int(input("Enter the day of month: 1-31: "))

j = y//100 
k = y%100

h = (q +(26*(m+1))//10 +k +k//4 +j//4 +(5*j)) % 7

week =["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"] #listofweeks
print("Day of week is: ", week[h] )



def calculate_isbn_10(first_9_digits):
    if len(first_9_digits) != 9 or not first_9_digits.isdigit():
        print("Incorrect input. It must have exactly 9 digits.")
        return None
    
    checksum = sum(int(first_9_digits[i]) * (i + 1) for i in range(9)) % 11

    last_digit = str(checksum) if checksum < 10 else 'X'

    isbn_10 = first_9_digits + last_digit

    return isbn_10


def calculate_isbn_10(first_9_digits):
    if len(first_9_digits) != 9 or not first_9_digits.isdigit():
        print("Incorrect input. It must have exactly 9 digits.")
        return None
    
    checksum = sum(int(first_9_digits[i]) * (i + 1) for i in range(9)) % 11

    last_digit = str(checksum) if checksum < 10 else 'X'

    isbn_10 = f"{first_9_digits}{last_digit}"

    return isbn_10


def find_max_occurrences():
    max_num = 0
    count = 0

  
    num = int(input("Enter an integer (enter 0 to end): "))

    if num == 0:
        print("No numbers entered.")
        return

    max_num = num
    count = 1

    while num != 0:
        num = int(input("Enter an integer (enter 0 to end): "))

        if num > max_num:
            max_num = num
            count = 1
        elif num == max_num:
            count += 1
