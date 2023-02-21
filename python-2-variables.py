Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x= 2
>>> y=3
>>> x+y
5
>>> x
2
>>> x+5
7
>>> x = 9
>>> x
9
>>> x +3
12
>>> x +y
12
>>> # a variable is a input which has a variable name ( in this case x and y ) and a value ( in this case 9 and 3 )
>>> x = 10
>>> x
10
>>> # variables are mutable that means it is change able
>>> 
>>> 
>>> 
>>> x + 10
20
>>> _+10
30
>>> # an underscore represent the previous value of the output . In this case it is 20
>>> 
>>> 
>>> x = 'sreedev'
>>> x
'sreedev'
>>> name = 'youtube'
>>> name
'youtube'
>>> x + name
'sreedevyoutube'
>>> name+' rocks'
'youtube rocks'
>>> #variable must always start with a letter and python is case sensetive
>>> 
>>> 
>>> name[0]
'y'
>>> name[]1
SyntaxError: invalid syntax
>>> name[1]
'o'
>>> #[index] number is used to fetch a charecter value from a variable
>>> 
>>> 
>>> 
>>> name[-1]
'e'
>>> name[-5]
'u'
>>> #while using a negative integer as a [index] number , it start's from backward
>>> 
>>> 
>>> 
>>> name[0:7]
'youtube'
>>> name[0:3]
'you'
>>> #[starting index number : ending index number (but that value is not included) ]
>>> 
>>> 
>>> 
>>> name[0:]
'youtube'
>>> name[:7]
'youtube'
>>> #by default , not keeping the [index] value of the starting will start from zero [index] number and not keeping the value of the ending [index] number , it will end at the the last charecter (last charecter is included)
>>> 
>>> 
>>> 
>>> name[3:10]
'tube'
>>> # by putting the value greater than the ending value will ultimately end at the last charecter
>>> 
>>> 
>>> 
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> # we conclude that strings in python are immutable
>>> 
>>> 
>>> 
>>> 'my' = name[3:10]
SyntaxError: can't assign to literal
>>> 'my' + name[3:10]
'mytube'
>>> 
>>> 
>>> 
>>> 
>>> name = 'mytube'
>>> name
'mytube'
>>> ### but the whole string are mutable but not just some charecter of its value
>>> 
>>> 
>>> 
>>> myname = ' sreedev '
>>> myname
' sreedev '
>>> len(myname)
9
>>> ### to find the length of the string we have to use a inbuild function called len() 
