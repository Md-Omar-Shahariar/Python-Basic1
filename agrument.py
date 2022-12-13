def argument(a, **d):
    print(a)
    print(d.items())
    for j,i in d.items():
        print(j,":",i)


argument("Afidi", age = 28, height = 5.5, weignt = 70)