#fibonacchi series
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

#sawp


def swap(c, d):
    print("before Swap: ", c, d)
    temp = c
    c = d
    d = temp
    print("After Swap: ", c, d)


swap(4, 5)

def swap1(c, d):
    print("before Swap: ", c, d)
    c = c + d
    d = c - d
    c = c - d
    print("After Swap: ", c, d)


swap1(1, 2)

def swap2(c, d):
    print("before Swap: ", c, d)
    c = c ^ d
    d = c ^ d
    c = c ^ d
    print("After Swap: ", c, d)


swap2(3, 4)

def swap3(c, d):
    print("before Swap: ", c, d)
    c, d = d, c
    print("After Swap: ", c, d)


swap3(6, 7)


