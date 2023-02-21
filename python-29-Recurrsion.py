###########-----------Recurrsion-----------#############

### Recursion means calling a function inside an function

def greet():
    print("Hello")
    greet() ### This is a recurrsion

    
#greet()

### To get the number of times the recurrsion have happened , we have to import sys

import sys

print(sys.getrecursionlimit())

def for_sys():
    print("Just for fun")
    for_sys()
    ### The result will be 1000

### To set the limit for a recurrsion , we have to do the following

sys.setrecursionlimit(100) ### enter the value we want to set the limit , 30 is the minimum limit 

print(sys.getrecursionlimit())

i = 0 ### To find the number of times recursion had happened manually
def from_sys():


    
    global i
    i = i+1
    print("set recurrsion limit",i)
    from_sys()

from_sys()



