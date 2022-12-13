from numpy import *

a = matrix([[1,2,3],[2,3,4]])
b = matrix([[1,2],[2,3],[3,4]])
c= a*b

print("Automated Calculation : \n", c)



d = array([[1,2,3],[2,3,4]])
e = array([[1,2],[2,3],[3,4]])

new  = zeros((2,2),int)

for i in range(0,2):
    for j in range(0,2):
     for k in range(0,3):
         new[i][j]+= d[i][k]*e[k][j]


print(new)
