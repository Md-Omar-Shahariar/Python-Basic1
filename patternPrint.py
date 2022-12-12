u = int(input("Enter Value:"))
for i in range(1,u):
    for x in range(1,u-i):
        print(" ",end="")
    for x in range(1,i+i):
        print("*",end="")

    print("\n")
for i in range(1, u):
    for x in range(1, i):
        print(" ", end="")
    for x in range(1,(u-i)*2):
        print("*", end="")

    print("\n")
