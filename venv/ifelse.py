# Leap Year
while True:
    Year = int(input("Please Enter a Year :"))

    if Year % 400 == 0 and Year % 100 == 0:
        print(Year, "Leap Year")
    elif Year % 4 == 0 and Year % 100 != 0:
        print(Year, "Leap Year")
    else:
        print(Year, "Not Leap Year")


