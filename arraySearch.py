from array import *

len = int(input("Please Enter The length of Array :"))

arr = array("i", [])

for i in range(len):
    arr.append(int(input("Enter The Value :")))

print("Array :", arr.tolist())
s = int(input("Enter the value you want to search : "))

try:
    print(arr.index(s))
except:
    print("Item Not Found")
