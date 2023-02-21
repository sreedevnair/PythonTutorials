x = input("Enter the first value")
y = input("Enter the second value")
z = x + y
print(z)

print("")

####this is because python is assumming x and y as a string value . Debug the above we have to do the following

a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
c = a + b
print(c)

print("")

### whenever a input function is used , by defult it is in the form of a string type

d = input("enter the first value")
q = int(d)
e = input("enter the second value")
r = int(e)
p = q + r
print(p)

print("")

### to prove that input function is in the form of string


g = input("enter the first value")
print(type(g))
h = input("enter the second value")
print(type(h))
i = g + h
print(i)

print("")

### Using charecter input

ch1 = input("Enter the charecter")
print(ch1)

print("")

### To fetch only first charecter

ch2 = input("Enter the charecter")
print(ch2[0])

print("")


### Another way of doing this is

ch3 = input("Enter the charecter")[0]
print(ch3)
### In this case the user can put infinity charecter , but the server will only print the first charecter or as we want

print("")

### Just an experiment

a1 = input("enter the charecter")
print(a1)

print("")

### to do such stuff , we have to use an thing called as (eval)

result = eval(input("enter the question"))
print(result)


        





