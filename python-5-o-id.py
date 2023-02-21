Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = 5
>>> id(nums)
1835361520
>>> name = 'sreedev'
>>> id(name)
69168800
>>> a = 10
>>> b = a
>>> id(id)
30423960
>>> id(a)
1835361600
>>> id(b)
1835361600
>>> name = 10
>>> name
10
>>> id(name)
1835361600
>>> 
>>> ### in pyhton , a variable having the same value will have the same address (id)
>>> id(10)
1835361600
>>> ###id is not base at the variable name , but the value it has
>>> k = 10
>>> id(k)
1835361600
>>> 
>>> 
>>> 
>>> ### changing the value of a
>>> a = 9
>>> id(a)
1835361584
>>> 
>>> b
10
>>> id(b)
1835361600
>>> ### b is still refering to 10
>>> 
>>> b = a
>>> b
9
>>> id(b)
1835361584
>>> k = 8
>>> k
8
>>> id(k)
1835361568
>>> id(name)
1835361600
>>> 
>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 
>>> 
>>> 
>>> ########-----------------------type----------------------------##########
>>> PI = 3.14
>>> type(PI)
<class 'float'>
>>> type(a)
<class 'int'>
>>> type(name)
<class 'int'>
>>> 
