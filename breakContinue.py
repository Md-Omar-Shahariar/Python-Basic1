x = int(input("How Many Candies :  "))

i = 1

while i <= x:

    if i % 3 ==0 or i % 5 == 0:
        pass
    else:
        print(i)
    i += 1


for y in range(1, x+1):
    if y % 2 == 0:
        pass
    else:
        print(y)