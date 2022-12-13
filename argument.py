def update(x):
    print("x before change : ", id(x))
    x = 8
    print("x after change :", id(x))
    print(x)



a=10
print("Id of a :",id(a))
update(a)
print("Id after change a", id(a))