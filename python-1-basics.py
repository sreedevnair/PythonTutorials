Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 2-4
-2
>>> 2*5
10
>>> 10/2 #this will give an float outcome
5.0
>>> 10//2 #using double division (/) , the float that is point zero will be removed
5
>>> 
>>> 2+2-4
0
>>> 2-4=2
SyntaxError: can't assign to operator
>>> 2-4+4
2
>>> 2+2*5 #first multiplication or division is done
12
>>> (2+2)*5 #using brackets we can do the same above
20
>>> 
>>> 2*2*2
8
>>> 2**4
16
>>> #using double stars or multiplication we can (raise to) some integer . here it the 2 (raised to) 4
>>> #spacing between anything will not bring any change
>>> 
>>> 310/2
155.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> #// this will also remove the remainder
>>> 10%3
1
>>> #using % this we will be able to find just the remainder
>>> 
>>> 
>>> 
>>> #string must be in double or single quotes " or '
>>> print('sreedev' 'laptop')
sreedevlaptop
>>> print('sreedev's' 'laptop')
      
SyntaxError: invalid syntax
>>> #to use apostrophy , there is only two ways
>>> print("sreedev's" "laptop")
sreedev'slaptop
>>> #first by using double quotes for strings and single quotes for apostrophy or visa versa
>>> print('sreedev\'\s laptop')
sreedev's laptop
>>> #using \ this we can tell python to ignore that special quotes or apostophy
>>> 
>>> 
>>> 'sreedev' + 'sreedev'
'sreedevsreedev'
>>> 'sreedev' *10
'sreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedev'
>>> 10* 'sreedev'
'sreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedevsreedev'
>>> #we can do this visa versa
>>> 
>>> 
>>> print('a:\blahhh\navin')
a:lahhh
avin
>>> #\n has a ability to break that line and \b has also a meaning
>>> print(r'a:\blahhh\navin')
a:\blahhh\navin
>>> #r means raw string and this will make the string as it is
