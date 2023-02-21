x = int(input("Enter the value"))
r = x%2
### (%) this modula operator is used to find the remainder

print("")

if r==0: ### this simply means to ask wheathe r is even or not
    print('even')
    if x>5 :
        print('x is greater than 5')

else :
    print('odd')

print("       ")

### we can use as many if statement as we want , using elif and else statement is more convenient

a = int(input("Enter the digit"))

if a<5:
    print("a is smaller than 5")
elif a==5:
    print("a is equal to 5")
else:
    print("a is greater than 5")
