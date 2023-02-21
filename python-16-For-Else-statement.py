nums = [10,13,12,14,117,26]

for x in nums:
    if x%5==0:
        print(x)
        break ### break is used to find the first number which is divisible by 5 and if it is found then the process breaks
    else :
        print('not found')
### this will print "not found" 5 times because , every time when the if statement checks for the first value of index that if it is divisible by 5 or not . If not is will print the else statement.
### and the process continue until the if statement gets finished

print(" ")        

### To solve the above , we must print the else statement outside the if statment
        
for x in nums:
    if x%5==0:
        print(x)
        break 
else :
    print('not found')

    
