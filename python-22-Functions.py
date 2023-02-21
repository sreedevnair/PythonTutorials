#########------------function in python----------###########

def greet():
    print("HELLO")
    print("GOOD MORNING")
    
greet()

### def means define

def addition_subtraction(x ,y):
    c =x+y
    d = x-y
    return c , d

result = addition_subtraction(5,5)
print(result)

print(" ")

############---------------------------###############

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print(x)

update(5) ### the value of the 5 will become 8

print(" ")

update(10)

a = 10
update(a) ### this will also print the value 8

print(" ")

print(a) ### but the value of a will not get changed and this output will show 10 , # a is still refering to 10

print(" ")

print(id(a)) ###########

print(" ")

print(id(10))
### Both will have the same id

### The following are the outcomes of the above

    #HELLO
    #GOOD MORNING
    #(10, 0)
     
    #1646421232
    #1646421280
    #8
     
    #1646421312
    #1646421280
    #8
    #1646421312
    #1646421280
    #8
     
    #10
     
    #1646421280
     
    #1646421312
### the final id of all update() will be the same






