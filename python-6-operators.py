Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> x=2
>>> y=3
>>> x+y
5
>>> x/y
0.6666666666666666
>>> 
>>> 
>>> 
>>> ### assingnment operator means assingning a value using = sign
>>> x = x+2
>>> x
4
>>> x +=2
>>> x
6
>>> x*3
18
>>> X*=3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    X*=3
NameError: name 'X' is not defined
>>> x*=3
>>> x
18
>>> a,b = 5,6
>>> a
5
>>> b
6
>>> 
>>> 
>>> ###############-----------------Unary operator--------------------#############################3
>>> n =7
>>> -n
-7
>>> n = -n
>>> n
-7
>>> 
>>> 
>>> ##########------------------Relation operators-------------------####################
>>> a<b
True
>>> a>b
False
>>> a == b
False
>>> ###we are using double equal to sign because we are not assingning the value of a to b
>>> ### we are just checking
>>> a = 6
>>> a == b
True
>>> a<=b
True
>>> a>=b
True
>>> a !=b
False
>>> ### ! means not , therefore when asked a not equal to b , it returned false
>>> b=7
>>> a
6
>>> a!=b
True
>>> 
>>> 
>>> ################-----------------logical operators------------------------#####################
>>> #### and , or , not
>>> a = 5
>>> b=6
>>> a<8 and b<9
True
>>> a<8 and b<2
False
>>> 
>>> a<8 or b<9
True
>>> a<8 or b<2
True
>>> 
>>> 
>>> 
>>> x = True
>>> not x
False
>>> y = False
>>> not y
True
>>> 
>>> #### (and) will only give true when both the statements are true or it will give false
>>> ### opposite of the above for (or)
>>> 
