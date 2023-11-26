def grade(score, best):
    if score >= best -10:
        return 'A'
    if score >= best -20:
        return 'B'
    if score >= best -30:
        return 'C'
    if score >= best -40:
        return 'D'
        return 'F'
  
  
score = input("Enter scores: ")
scores = [ int(s) for s in score.split()]
best = scores[0]
for i in range(len(scores)):
    if scores[i] > best:
        best = scores[i]

for i in range(len(scores)):
    print ("Student", i, "score is", scores[i], "and grade is", grade(scores[i], best))


score = int(input("Enter scores: "))
scores = [sc for sc in score.split()]
best = scores[0]
for i in range(len(scores)):
    if scores[i] > best:
        best = scores[i]


def count_frequency(list_of_values):
    
    d = dict()
    
    for value in list_of_values:
        if not value in d.keys():   
            d[value] = 1           
        else:
            d[value] += 1        

    return d

input_string = input("Enter integers between 1 and 100, inclusive: ")

values = [int(x) for x in input_string.split(" ")]

value_count_dictionary = count_frequency(values)

keys = []
for x in value_count_dictionary.keys():
    keys.append(x)

keys.sort()

for value in keys:
    print(value, "occurs",value_count_dictionary[value], "time" if value_count_dictionary[value] == 1 else "times")


numbers = input("Enter your numbers: ")
list1 = numbers.split()
list2 = []
for i in range(len(list1)):
    if not list1[i] in list2:
        list2.append(list1[i])
print("The distinct numbers are: ")
for i in range(len(list2)):
    print(list2[i], end=' ')
print()

-----------------------------
def mean(list):
    l = len(list)
    i = 0
    sum = 0
    while i<l:
        sum += list[i]
        i+=1
    return sum/l

def standardDeviation(list):
    m = mean(list)
    l = len(list)
    i = 0
    sum = 0
    while i<l:
        sum += (list[i]-m)*(list[i]-m)
        i+=1
    sum = sum / (l-1)
    return sum**0.5

def main():
    nums = input("Enter numbers: ")
    lst = [float(x) for x in nums.split(" ")]
    print("The mean is",mean(lst))
    print("The standard deviation is",standardDeviation(lst))

main()

def isSorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

user_input = input("Enter list: ")
numbers = [int(num) for num in user_input.split()]

if isSorted(numbers):
    print("The list is already sorted")
else:
    print("The list is not sorted")
    

def isAnagram(s1,s2):
    lst1 = []
    lst2 = []

    for x in s1:
        lst1.append(x)
         
    for x in s2:
        lst2.append(x)
   
    lst1.sort()
    lst2.sort()

    if(len(lst1)!=len(lst2)):
        return False
    else:
        for x in range(len(lst1)): 
            if(lst1[x]!=lst2[x]): 
                return False
        return True

def main():
 
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
  
    if(isAnagram(s1,s2)):
        print("The words",s1,"and",s2,"are anagrams")
    else:
        print("The words", s1, "and", s2, "are not anagrams")

main()