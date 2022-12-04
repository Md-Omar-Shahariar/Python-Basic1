# numbers
d = 2
c = 3
s = c + d

print(d + c)

print("Sum : ", s)

print(r"c:ad\newFolder")
print("c:ad\newFolder")

# Strings

str = "Afridi"
str = str + "01"


print(str[3:])
print(str[1:3])

# list

list = [1, 2, 6, 4, 5]
print(list.count(3))
print(list.pop())
list.sort()
print(list)
list.append(5)
list.sort()
print(list)
list.extend([7, 8, 9, 10])
print(list)
list.insert(0, 0)
print(list)
list.remove(10)
print(list)
print(list.index(9))
list.reverse()
print(list)

# Set
set = {1, 2, 3, 5, 4, 3}

print(set)

print(set)
# Tuple
tup = (1, 2, 3, 4)
print(tup.count(1))

# Dictionary

data = {"Java": {"SE": "NetBeans", "EE": "Eclipes"}, "Python": ["Pycharm", "Sublime"], "JS": "VScode"}

print(data)
print(data["Java"]["SE"])
print(data["Python"][1])
print(data["JS"])

print(id(str))

#data types
#None Type
none = None
print(type(none))

#Numeric Type
a = 3
print(type(a))
b = 4.0
print(type(b))
b=int(b)
print(type(b))
c = complex(a, b)
print(c)
print(type(c))
boo = a>b
print(type(boo))

#List
#set
#tuple
#String
#range type
for i in range(0,5):
    print((i))


#dictionary

dicto = {"a": "12", "b": {"1": "c", "2": "v"}}
print(dicto.keys())
print(dicto.values())
print(dicto["b"]["2"])

#logical operators
print(2<4 or 3>4)
print(2<4 and 3>4)
print(not 0)
#number system conversion

binary = bin(25)
print(binary)
octal = oct(25)
hexa = hex(25)
print(octal)
print(hexa)
print(0b1001)
