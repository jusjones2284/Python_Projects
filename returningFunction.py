
def main():
    list1 = m(1)
print(list1)
list2 = m(1)

    

def m(x, lst = [1,1,2,3]):
    if x in lst:
        lst.remove(x)
        return lst

def f(i, values = []):
    values.append(i)
    return values

f(1)
f(2)
v = f(3)    