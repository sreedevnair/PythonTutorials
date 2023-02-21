##########-------------Array in python-------------##########

### In pyhton , we have to mention the type of array is , not like simple in list or tuples
### We should have a array of the same type.

from array import * ### * means that we have to import all the materials from that modules.

vals = array('i' , [3,5,6,2,5])

### python have a certain types of typecode which we have to mention in an array .
### Her i means signed integer

print(vals)
print(vals.buffer_info())
### .buffer_info() will give us the address of the array first and then the size of the array
print(vals.typecode)
### this will give us the type of the value

### we can add values to the array using append function and remove some values using remove or pop

vals.reverse()
print(vals)
### To reverse an array we have to mention that array seperately

### We can also use index number to find the value od the array
print(vals[0])

### To print all the value seperately

for i in range(5):
    print(vals[i])

### when we do not know the length of that array  ,we can do the below

for i in range(len(vals)):
    print(vals[i])

### Another way of doing this is

for e in vals:
    print(e)

### Whne we have to copy a array to a new array

newARR = array(vals.typecode , (a for a in vals))
### We are telling python to first copy the type of code of vals and then for a in vals print(a) , this print(a) has to come at first

print(newARR)

### to copy the square of the old array

newARR = array(vals.typecode , (a*a for a in vals))
print(newARR)

### Another way of doing this is using for loop

for a in newARR:
    print(a*a)

### using while loop

i =0
while i<len(vals):
    print(vals[i])
    i = i+1
    



    
