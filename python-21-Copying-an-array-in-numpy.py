##########---------Copying an array in numpy---------#############

from numpy import *

arr = array([1,2,3,4,5])

for e in arr:
    print(arr+5)
    break

### another way of doing this is

arr1 = arr+5
print(arr1)

### we can also add two arrays

print(concatenate([arr,arr1])) ### concatenate means simply add

### Coping an array

arr2 = array([1,3,5,7,9])

arr3 = arr2

print(arr3)
print(arr2)


print(id(arr2))
print(id(arr3))
### both will have the same id
### This meathod is called as Alising

print("")

### To solve this we have to use the following function

arr4 = array([2,4,6,8,0])
arr5 = arr4.view() ###.view will give that array an a different id

print(arr4)
print(arr5)

print(id(arr4))
print(id(arr5))

### Another type of copying is called shallow copying

arr6 = array([1,2,3,4,5])

arr7 = arr6

arr6[1] = 7 

print(arr6)
print(arr7)

print(id(arr6))
print(id(arr7))
### In this type of copying when we change the value of the first array  , the value of teh second value will also get changed

### Next way of doing this deep copying

arr8 = array([6,7,8,9,0])

arr9 = arr8.copy()

arr8[1] = 2

print(arr8)
print(arr9)

print(id(arr8))
print(id(arr9))

### id of the both the array in shallow copying will be the smae but different for the value in deep copying


