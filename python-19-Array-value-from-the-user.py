############--------Array values from the user----------###############

from array import *

arr = array('I', [])

n = int(input("Enter the lenght of the array"))

print(" ")

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)

print(" ")

### to get the index niumber from the user and give back the value 
a = int(input("Enter the index number"))

print(" ")

if a<=n:
    print(arr[a])
else :
    print("Index value out of the range")

print(" ")

### TO get the value from the user and then printing the index number

val = int(input("Enter the value"))

print(" ")

k = 0
for e in arr:
    if e==val:
        print(k)
        break
    k = k+1
    
if e!=arr:
    print("value not found")

print(" ")

print(arr.index(val))
