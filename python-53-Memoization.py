##########-------Memoization-------##########

### Memoization means that to store an output and then use it when given the same input

import time
### time module is used to give a break for a specific time period

def memo(n):
    print("Computing",n,'.....')
    time.sleep(1) ### This will give a break of 1 second
    return n*n

print(memo(4))

print(memo(10))

print(memo(4))

print(memo(10))

### This whole process will take 4 seconds

print('')

### To do the same with Memoization

ef_cache = {} ### We are creating an empty dictionary

def memo(n):
    
    if n in ef_cache: ### This will take the key
        return ef_cache[n] ### This will give us the value
    
    print("Computing",n,'.....')
    time.sleep(1)

    ef_cache[n] = n*n ### We are adding the value to the key here
    return n*n

print(memo(4))

print(memo(10))

print(memo(4))

print(memo(10))

