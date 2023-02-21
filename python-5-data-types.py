Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### data types in python are : None , Numeric , List , Tuples , Set , String , Range , Dictionary/Map
>>> 
>>> 
>>> 
>>> ### When a variable is not assigned any value , its data type is NONE
>>> ###
>>> 
>>> ### Numeric are classified in four more catagory : int , float , complex , bool
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> n = 5
>>> type(num)
<class 'float'>
>>> type(n)
<class 'int'>
num = 5 + 6j
>>> type(num)
<class 'complex'>
>>> ### j is a imaginary number and 5 and 6 are real number
>>> 
>>> 
>>> 
>>> ### to convert a float value to int ,  you must do the following things
>>> a  =5.6
>>> int(a)
5
>>> ### hence using int(variable) , we can convert an float into ia integer
>>> 
>>> ###to convert int into float
>>> a
5.6
>>> b = int(a)
>>> b
5
>>> float(b)
5.0
>>> k = float(b)
>>> k
5.0
>>> 
>>> 
>>> ### to convert into complex
>>> k = 6
>>> c = complex(b,k)
>>> c
(5+6j)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #########-------------------------boolean----------------------------###############33
>>> 5<6
True
>>> a = 4>2
>>> a
True
>>> type(a)
<class 'bool'>
>>> b = 6>8
>>> b
False
>>> 
>>> 
>>> 
>>> ### in python boolean (true or false) when converted to int , it is in the format 1 and 0 respectively
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(False)
0
>>> int(b)
0
>>> int(a)
1
>>> 
>>> 
>>> ### List , tuples , set , string , range are comes in the catagory of sequence
>>> lis = [25,26,22,24]
>>> type(lis)
<class 'list'>
>>> s = {23,23,25,46,15}
>>> type(s)
<class 'set'>
>>> t = (23,25,26,26)
>>> type(t)
<class 'tuple'>
>>> str = 'sreedev'
>>> type(str)
<class 'str'>
>>> 
>>> 
>>> 
>>> ###############----------------range-----------------########################
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> range
<class 'range'>
>>> 
>>> list(range(2,11,2))
[2, 4, 6, 8, 10]
>>> ### range(start, end , difference/skip)
>>> 
>>> 
>>> 
>>> #########################---------------------dictionary/mapping-----------------------########################

>>> dic1 = {'sreedev':'oneplus','mahi':'nokia', 'gurpreet':'iphone'}
>>> dic1
{'sreedev': 'oneplus', 'mahi': 'nokia', 'gurpreet': 'iphone'}
>>> dic1.keys()
dict_keys(['sreedev', 'mahi', 'gurpreet'])
>>> dic1.values()
dict_values(['oneplus', 'nokia', 'iphone'])
>>> 
>>> dic1['sreedev']
'oneplus'
>>> dic1.get('sreedev')
'oneplus'
>>> ### curly brackets is used to not repeat any values or keys
