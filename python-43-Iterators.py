#########---------Iterator---------#########

nums = [7,3,9,5]

for i in nums:
    print(i)
    
print(" ")

### Another way of doing this is by using Iterators

it = iter(nums) ### to use iterator we have to use the function called as iter

print(it.__next__()) ### This will print first value
print(it.__next__())### This will print next value , that is the second value
print(it.__next__()) ### This will print next value , that is the third value

print(next(it)) ### This will print the next value, that is the fourth value

#### How to create our own __next__() function

class topten:

    def __init__(self):
        self.num = 1


    def __iter__(self):
        return self

    def __next__(self):

        if self.num<=10:
            
            vals = self.num
            self.num += 1
            return vals

        else :
            raise StopIteration

values = topten()

print(next(values))

print(" ")

for i in values:
    print(i)
