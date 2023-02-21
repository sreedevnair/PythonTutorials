########-----------Linear Search-------###########

def search(list,n):
    i = 0
    while i<len(list):
        if list[i] == n:
            print(i)
            return True     
        i = i+1  
    return False
            
list = [5,8,4,6,9,2]
n = 9


search(list,n)

if search(list,n):
    print("Found " )
else:
    print("Not Found")
    
print('')

### Another way of finding the position is that by doing the following

pos = "something"

def search(list,n):
    i = 0
    while i<len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True     
        i = i+1  
    return False
            
list = [5,8,4,6,9,2]
n = 9

if search(list,n):
    print("Found at", pos )
else:
    print("Not Found")

### We can use pos insude the if statement because we defined pos at the first and then we changed the value inside a fuction
### We have changed a global variable to a local variable by mentioning the above things

print("")
##### How to do the same by using for loop

pos = "something"

def search(list,n):
    
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals() ['pos'] = i
            return True       
    return False
            
list = [5,8,4,6,9,2]
n = 6

if search(list,n):
    print("Found at", pos )
else:
    print("Not Found")
