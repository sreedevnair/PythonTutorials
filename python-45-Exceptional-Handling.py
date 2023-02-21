########--------Exceptional Handling--------#########

a = 5
b = 0

try:
    print(a/b)
except Exception:
    print("There is a error")

print("Bye")

### By using try: we tell the python to check and execute the statement if it is true else .
### If we gets the statement wrong , normaly we gets an error and the python stops to excute futher statements.
### But by using except Exception: we can write what we want if the statment above throws an error

print(" ")

c = 6
d = 0

try:
    print(c/d)
except Exception as e:
    print("There's an error and" , e)

### Using as e , python will aslo give his error with the line we wrote while throwing an error

print(" ")

e = 6
f = 0

try:
    print("Resource Opened")
    print(e/f)
except Exception as e:
    print("There's an error and" , e)
finally:
    print("Resource Closed")
### (finally) block will be executed if we get error as well as if we don't het the error

### we can use as many except as we want 
