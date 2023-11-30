
from tkinter import Y
from unittest import result


list2 = "Hello world! On my way to charleston".split(" ")
list3 = []
def printList(list1):
    for element in list1:
        list3.append(element)

# printList(list2)
# print(list3)

def main():
    x = 1
    y = [1,2,3]
    m(x, y)
    print("x is", x)
    print("y[0] is", y[0])
    return x, y


def  m(number, numbers):
    number = 1001
    numbers[0] = 5555
    
    
    
main()

def mains():
    number = 0
    numbers = [10]
    n(number, numbers)
    



def n(x, y):
    x = 3
    y[0] = 3


def reverse(lst):
    result = [0] * len(lst)
    
    for i in range(0, len(lst)):
        result[i] = lst[len(lst) - 1 - i]
        
        return result
    
list5 = [1,2,3,4,5,6]
list2 = reverse(list5)
