Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###########------------Import Math Functions--------------##########################
>>> import math
>>> math.sqrt(25)
5.0
>>> math.sqrt(15)
3.872983346207417
>>> 
>>> 
>>> 
>>> math.floor(2.9)
2
>>> math.floor(2.2)
2
>>> math.floor(2.5)
2
>>> ### using .floor function in math , we can get the least round off
>>> 
>>> math.ceil(2.1)
3
>>> math.ceil(2.5)
3
>>> math.ceil(2.9)
3
>>> ### using .ceil function in math , we can get the last (largest) round off
>>> 
>>> 
>>> 
>>> 3 ** 2
9
>>> 3 ** 4
81
>>> 3*3*3*3
81
>>> math.pow(3,2)
9.0
>>> math.pow(3,3)
27.0
>>> math.pow(3,4)
81.0
>>> ### using .pow which represent power in math , we can get the power of an integer (integer,raise to)
>>> 
>>> 
>>> 
>>> math.pi
3.141592653589793
>>> 
>>> 
>>> 
>>> ### another short way to do this is the following
>>> 
=============================== RESTART: Shell ===============================
>>> #############-----------------Import Math Function----------#################
>>> import math as m
>>> m.sqrt(25)
5.0
>>> math.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    math.sqrt(25)
NameError: name 'math' is not defined
>>> m.pow(3,5)
243.0
>>> 
>>> 
>>> 
>>> ### when we want to import a particular function in math , we can do the following
>>> 
=============================== RESTART: Shell ===============================
>>> from math import sqrt,pow
>>> pow(3,2)
9.0
>>> sqrt(25)
5.0
>>> floor(2.9)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    floor(2.9)
NameError: name 'floor' is not defined
>>> 
>>> ### we can not use the floor function because we had not imported it
>>> 
>>> ### when we use (from ......import...) we can use the funtion without mentioning the name of the function
>>> 
