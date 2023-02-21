Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (21 , 24 , 54 , 62 , 68)
>>> tup[0]
21
>>> tup[4]
68
>>> 
>>> tup[0] = 34
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[0] = 34
TypeError: 'tuple' object does not support item assignment
>>> ### tuples are immutable
>>> 
>>> tup.count(21)
1
>>> tup.count(54)
1
>>> ### .count is used to find the number of times a value has repeated
>>> 
>>> tup.index(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tup.index(0)
ValueError: tuple.index(x): x not in tuple
>>> tup.index(54)
2
>>> ### .index is used to find the [index] number of that input
>>> 
>>>  
>>>
###################################--------------------{SETS}-----------------------------------########################################3333
>>> 
>>> s = {22 , 23 , 24, 11 ,12 ,104 ,24 }
>>> s
{104, 11, 12, 22, 23, 24}
>>> ### sets must be in a curly brackets {} . Sets removes the repeated number and also change the sequence randomly
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> ### sets don not support indexing because it has got random undex value
>>> s = {24 ,73, 79}
>>> s
{24, 73, 79}
>>> ### sets are mutable
>>> 
