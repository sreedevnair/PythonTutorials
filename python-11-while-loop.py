#######------------While loops in pyhton----------#############

###while loop is used to repeat things multiple times

### Fist step is to provide a counter
i = 1
###second is to use the while loop 

while i<=5: ###while i is smaller or equal to zero , print('sreedev') 
    print('sreedev')
    i = i+1 ### This will increase the value of i with respect to one
### What happened is that , the while loop will first check the value of i to be smaller or equal to 5 , if it is smaller or equal to 5 it will print ('sreedev') , then as we had mentioned , it will increase the value of i and will restart the while loop until i becomes 6 or greater than 6
print(' ')
###WE can do this same thing in a reverse order

k = 5    

while k>=1:
    print('Suresh')
    k = k-1

print(" ")

i = 1

while i<=5:
    print('sreedev', i)
    i = i+1 
### this will print the value of i also

print(' ')

### to use a nested while loop

i = 1
j= 1

while i<=5:
    print('sreedev ')
    while j<=5:
        print('rocks ')
        j = j+1
    i = i+1 
### what is happening is that , the j in nested while loop needs to get completed first

print('  ')

i = 1

while i<=5:
    print('sreedev ')
    a = 1
    while a<=5:
        print('rocks ')
        a = a+1
    i = i+1 
### Hence will make rocks print 4 times seperately

print("")

i = 1

while i<=5:
    print('sreedev', end="" )
    a = 1
    while a<=5:
        print('rocks ', end="")
        a = a+1
    i = i+1 
###Using (end) will make the whole while loop in one line

print(" ")

print("")

i = 1

while i<=5:
    print('sreedev ', end="")
    a = 1
    while a<=5:
        print('rocks ', end="")
        a = a+1
    i = i+1
    print()
### What we are doing is that , we are printing the loop when it gets completed first time    


