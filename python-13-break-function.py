############----------Break function in python----------############

x = int(input("Enter then number of smartphones you need"))
av = 5 ### av means available
i = 1

while i <= x:
    print("smartphone")
    if i>av:
        print('Out of stock')
        break
    i = i+1

print(" ")


print("Thank You")


### First the user will give the amount of smartphone it needs , then while loop will check wheather the amount is greater than 1 or not .
### If yes , it will print smartphone , then it will check whether i is greater than av , if it is then it will print out of stock and will break the while loop
###If not it will run the while loop until it becomes greater than av
### We cannot put the if statement after the i is increased because the if statement is under the control of the value i
    

