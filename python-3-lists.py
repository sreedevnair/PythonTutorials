Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [25 , 12 ,29 , 24 , 23 ,45]
>>> nums
[25, 12, 29, 24, 23, 45]
>>> ### this is a example of list[]
>>> nums[0]
25
>>> nums[5]
45
>>> ### to fetch a charecter from a list [index] number is used as we use it in for strings
>>> nums[2:8]
[29, 24, 23, 45]
>>> name[2:]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name[2:]
NameError: name 'name' is not defined
>>> nums[2:]
[29, 24, 23, 45]
>>> nums[-1]
45
>>> nums[-2]
23
>>> 
>>> 
>>> 
>>> names = ['kiran' , 'sreedev' , 'sreenath']
>>> names[0]
'kiran'
>>> name[2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name[2]
NameError: name 'name' is not defined
>>> names[2]
'sreenath'
>>> 
>>> 
>>> 
>>> values = [24 , 'sreedev' , 2.5]
>>> values
[24, 'sreedev', 2.5]
>>> 
>>> 
>>> ### lists[] in python are flexible which means it can hold srting , integer and float numbers
>>> 
>>> 
>>> mil = [nums , names]
>>> mil
[[25, 12, 29, 24, 23, 45], ['kiran', 'sreedev', 'mahi']]
>>> mil = nums + names
>>> mil
[25, 12, 29, 24, 23, 45, 'kiran', 'sreedev', 'mahi']
>>> ### study the above pattern carefully
>>> 
>>> 
>>> nums.append(100)
>>> nums
[25, 12, 29, 24, 23, 45, 100]
>>> ### using .append(input) , the input will be added as a value at the end of the list
>>> 
>>> nums.insert(0, 199)
>>> nums
[199, 25, 12, 29, 24, 23, 45, 100]
>>> ### using .insert(input) , the input will be added as a value at the [index] number we mentioned at the starting of the input to the list
>>> 
>>> nums.remove(199)
>>> nums
[25, 12, 29, 24, 23, 45, 100]
>>> ### study the above carefully
>>> 
>>> nums.pop(0)
25
>>> nums
[12, 29, 24, 23, 45, 100]
>>> nums.pop(0)
12
>>> nums
[29, 24, 23, 45, 100]
>>> ### .pop is used to remove a value using its [index] number
>>> nums.pop()
100
>>> nums
[29, 24, 23, 45]
'
>>> ### when an input is not mentioned it will automatically remove the ending value
>>> 
>>> 
>>> del nums[2:]
>>> nums
[29, 24]
>>> ### using del function we can remove more than one value fron the input just by mentiong the [index] number
>>> 
>>> nums.extend([24 , 23 ,44 ,55 , 67])
>>> nums
[29, 24, 24, 23, 44, 55, 67]
>>> 
>>> 
>>> min(nums)
23
>>> max(nums)
67
>>> ### using the above function we can find the minimum and the maximum value of the list
>>> 
>>> 
>>> nums.sort
<built-in method sort of list object at 0x0347D210>
>>> nums
[29, 24, 24, 23, 44, 55, 67]
>>> nums.extend([26 , 9])
>>> nums
[29, 24, 24, 23, 44, 55, 67, 26, 9]
>>> 
>>>  
>>> nums.sort
<built-in method sort of list object at 0x0347D210>
>>> nums
[29, 24, 24, 23, 44, 55, 67, 26, 9]

### we have to use brackets aftern writing the sort inbuild function

