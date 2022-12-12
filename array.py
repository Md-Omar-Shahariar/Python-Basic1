from array import *
a = array("i",[1,2,3])
a.append(3)
a.reverse()
print(a[2])

for i in range(len(a)):
    print(a[i], end="")
b = [x for x in a]
print(b)

newArray = array(a.typecode,(x for x in a))
print(newArray)
for x in newArray:
    print(x)