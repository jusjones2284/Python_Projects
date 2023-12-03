t1 = (1,3,5)

t2 = ()
t3 = tuple([2 * x for x in range(1,5)])
print(t3)

t4 = tuple("abac")
print(t4)

x = 'y'

print(x in t4)
len(t4)


tuple1 = ("green", "red", "blue")
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5])
print(tuple2)

print("length is", len(tuple2))
print("max is", max(tuple2))
print("min is", min(tuple2))
print("sum is", sum(tuple2))

tupple3 = tuple2 + tuple1
print(tupple3)
print(3 * tupple3)
print(tupple3[2:6])
print(tupple3[-1])
print(2 in tupple3)





def tupFun(tup):
  print(max(tup))


tupFun(tuple1)
tupFun(tuple2)

for v in tupple3:
  print(v, end=" ")

print([x for tupple3 in range(2) ])

list5 = list(tupple3)
# list5.sort(tuple1)
list6 = tuple(list5)

t22 = 4, 5, 1
k = list(t22)
k.sort()
print("t22 is ", (k))

t23 = (5, 1, 3, 10)
print("t23 is ", t23)

