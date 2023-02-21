########--------Global Keywords------############

a = 10
### Variable value outside the function is called Global 
def something():
    a = 15
    print("In the fuction",a)
### Variables inside a function are called Local
    
something()              

print("Outside the function",a)

def something():
    print("In the fuction",a)
    ### we can also use global keywords inside a function also when a local keyword is not mentioned
something()

### To use a global variable inside a function , we have to do the following method

def something():
    global a ### Using this , the python will convert the value of the global to the value mentioned inside the function
    a = 15
    print("In the fuction",a)
    
something()
print(a)

### A function always gives the local keyword the first priority
