# def linearSearch(lst, key):
#     for i in range(len(lst)):
#         if key == lst[i]:
#             return i
        
#     return -1

# def main():
#     lst = [4, 5, 1, 2, 9, -3]
#     print(linearSearch(lst, 2))

# main()

# def binarySearch(lst, key):
#     low = 0
#     high = len(lst) - 1
    
#     mid = (low + high)/2
#     if key < lst[mid]:
#         return mid 
#     elif key == lst[mid]:
#         return mid; 
#     else:
#         low = mid + 1

# lst = [1, 2, 3, 5, 4]

# for i in range(len(lst)):
#     temp = lst[i]
#     lst[i]

def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = min(lst[i:])
        currentMinIndex = i + lst[i:].index(currentMin)
        
