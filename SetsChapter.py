x = [] #list
x1 = () #tuple
x2 = set() #sets dosent allow duplicates and puts in any order

summerMonths = {"Jun", "Jul", "Aug"}
randomNumbers = {10, 50, 20, 1}
randomNumbers1 = {15, 51, 32, 20, 5}

fallMonths = set(("Sept", "Oct", "Nov"))

winterMonths = set()
winterMonths.add("Dec")
winterMonths.add("Jan")
winterMonths.add("Feb")

springMonths = {"Mar", "Apr", "May"}

summerMonths.add("Sept")
fallMonths.add("Dec")
winterMonths.add("Mar")
springMonths.add("Jun")

startFall = fallMonths.intersection(summerMonths)
startOne = randomNumbers.intersection(randomNumbers1)
print(startOne)
print(startFall)
print(winterMonths)

changeMonths = fallMonths.intersection(summerMonths)
print(changeMonths)
changeMonths = changeMonths.union(fallMonths.intersection(winterMonths))
print(changeMonths)
changeMonths = changeMonths.union(springMonths.intersection(summerMonths))
changeMonths =changeMonths.union(winterMonths.intersection(springMonths))
print(changeMonths)


s32 = {1,3,5}
s20 = set()
s24 = set((4,56,2))
s34 = [x * 2 for x in range(1,10)]
s36 = [x * 50 for x in range(1,10)]
print(s36)

s100 = {50,85,1}
s100.add(6)
len(s100)
max(s100)
4 in s100
# s100.remove(4)
s101 = s100
print(s100.issubset(s101))


