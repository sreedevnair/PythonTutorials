#######-----Lambda-------########

### Lambda means one line function that does not have a name

### Normal fuctions are as follows

def square(a):
    print(a*a)

square(5)

### Now using lambda function

f = lambda a : a*a
### first we are give the lambda function an identity then using (a) as a paramenter in a normal function and then giving a colon that means return 

print(f(5))
