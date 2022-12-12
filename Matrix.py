from numpy import *

arr = array([[1,2,3,4,5,6],[3,4,5,6,7,8]])

arr2 =arr.flatten()
print(arr)
print(arr2)
print("3D Array :\n", arr2.reshape(2,2,3))


arr1 = array([[1,2,3],[2,3,4]])
arr3 = array([[1,2,3],[2,3,4]])
arr4 = arr1*arr3
print(arr4)

m = matrix("1 2 3 ; 4 5 6 ; 7 8 9")

print("Matrix :\n\t", m)
print("diagonal :\n\t ",diagonal(m))