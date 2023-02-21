#########------Filter-------#######

def is_even(n):
    return n%2==0

nums = [1,3,2,6,4,9,6,8]

evens = list(filter(is_even,nums))

print(evens)

### Using lambda fuction



nums1 = [2,5,32,7,5,3,7,0]

even = list(filter(lambda a : a%2==0,nums1))

print(even)

########-------Map-------##########

double = list(map(lambda f : f*2,evens))

print(double)
### this can also be done by using normal function

#########-----------Reduce----------##############

from functools import reduce

sum1 = reduce(lambda a,b:a+b,evens)

print(sum1)
