
# Alogrithm 1

### Take an input of n and return the sum of the numbers from 0 to n

def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum = x + final_sum
        
    return final_sum

print(sum1(5))

             #or

def sum2(n):
    print(n*(n+1)//2)

sum2(5)

# Algorithm 2

### Print the first item in a list of values

def get1(valuse):
    print(valuse[0])

get1([4,2,7,9,3])

# Algorithm 3

### Takes in a list and pritn out all the values

def getall(values):
    for i in values:
        print(i)

getall([1,'Sreedev','Sreenath',6,9])

# Algorithm 4

### Prints pairs for item in list

def pair(values):
    k = 0
    if len(values)%2 != 0:
        print('Length is not even')
    else :
        for i in values:
            print(values[k], values[k+1])
            k = k+2
            if k == len(values):
                break

pair([1,3,2,6,4,8])

print("")

# Algorithm 5

###  Prints pairs for "EVERY" item in list

def pair_all(values):
    for item_1 in values:
        for item_2 in values:
            print(item_1 , item_2)
        
pair_all([1,3,6,4])

# Algorithm 6

### Print all items three times

def print_3(n):
    for i in n:
        print(i)
    for i in n:
        print(i)
    for i in n:
        print(i)
        
print_3([1,2,3])

print("")

                #or

def print3(n):
    for i in range(3):
        for i in n:
            print(i)
        
print3([1,2,3])

# Algorithm 7

### Given a list , return a boolean indicating if match item is in the list

def matcher(n,match):

    for item in n:
        if item == match:
            return True
    return False

if matcher([2,4,6,3,8],7):
    print('True')
else:
    print('False')

# Algorithm 8

### Print "Hello World" n times

def HW(n):
    for i in range(n):
        print('Hello World')

HW(10)

# Algorithm 9

### Write a function for anagram

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    # First we are replacing all the spaces between , the we are converting every letter in into lower case

    return sorted(s1) == sorted(s2)

if anagram('dog','god'):
    print("True")
else:
    print("False")

print("")

# Algorithm 10

### Give an integer array , output all the unique pairs that sum up to a specific value k

def pair_sum(array, k):
    if len(array) < 2:
        return print('Too small')
    
    seen = set()
    output = set()

    for num in array:
        target = k - num
        
        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num,target),max(num,target)))
    print('n'.join(map(str, list(output))))


pair_sum([1,2,5,3],4)

# Algorithm 11

### Take an array with positive and negative integers and find the maximum sum of that array

def largest(arr):
    if len(arr) == 0:
        print('Two Small')
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

print(largest([1,8,4,5,6,7,3,2,11,-10]))

# Algorithm 12

### Given a string of words , reverse all the words

def reverse(s):
    s = s.split()
    s.reverse()
    print(s)

reverse('This is the best')

              #or

def reverse2(s):
    return "-".join(s.split()[::-1])

print(reverse2('This is the best'))

              #or

def reverse3(s):
    return print(s.split()[::-1])

reverse3("HELLO , I AM SREEDEV")

# Algorithm 13

### Given 2 arrays (assume no duplication) , 1 array is a rotation of another - return True/False. Select an indexed position zand gets its value , Find same element in list2 and check index for index from there
### If any variation then we know its false, Getting to last item without a false means true

def rotation(list1,list2):
    
    if len(list1) != len(list2):
        return False
    
    key = list1[0]
    key_index = 0
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i

            break 

    if key_index == 0:
        return False

    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)

        if list1[x] != list2[l2index]:
            return False

    return True

print(rotation([1,2,3,4,5,6,7],[4,5,6,7,1,2,3]))

# Algorithm 14

### Return the common elements (as an array) between two sorted arrays of integers (ascending order)

def common(a , b):
    p1 = 0
    p2 = 0

    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1]) # we can use (b[p2])
            p1 = p1 + 1
            p2 = p2 + 2

        elif a[p1] > b[p2]:
            p2 = p2 + 1

        else:
            p1 = p1 + 1

    return result

print(common([1,2,4,6,8,5],[1,8,4,5,6,2]))

# Algorithm 15

### Given an array , what is the most frequently occuring element

def most_frequent(list):
    count = {}
    max_count = 0
    max_item = None

    for i in list:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1
            
        if count[i] > max_count:
            max_count = count[i]

            max_item = i

    return max_item

print(most_frequent([1,3,5,4,3,5,2,9,1,1]))

# Algorithm 15

### Given a string , are all characters unique . Should give True or false return

def unique(string):
    string = string.replace(' ','')
    return len(set(string)) == len(string) ### A set will remove all the dupliction

print(unique('a b cdef'))

            # without using inbuild function

def unique(s):
    s = s.replace(' ','')
    character = set()

    for letter in s:
        if letter in character:
            return False
        else:
            character.add(letter)
    return True

print(unique('a b cdef'))

# Algorithm 16

### Take a string and return charecter that never repeat , if multiple uniques then return only the first unique

def non_repeating(s):
    s = s.replace(' ','').lower()

    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c]+= 1

        else:
            char_count[c] = 1

    for c in s:
        if char_count[c] == 1:
            return c

    return None

print(non_repeating('I Apple Ape Pees'))
            
                # When we need to return all the uniques

def non_repeating(s):
    s = s.replace(' ','').lower()
    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c]+= 1
        else:
            char_count[c] = 1

    all_uniques = []
    y = sorted(char_count.items(), key = lambda x: x[1])

    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item)
            
    return all_uniques

print(non_repeating('I Apple Ape Pees'))






            
    


