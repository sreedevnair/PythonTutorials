##########-----------Numpy in python----------###########

### the normals array we use is one D .
### to use 2D array we have to use two square brackets

from numpy import *

### In numpy we dont have to mention the type of the integer like i or I in normal array (optinal)

ARR = array([2,3,4,5,6,2,7,8,9,0,1,])
print(ARR)

### If we want to mention the type of the value we have to do it in the last

ARR1 = array([1,2,3,4,5,6,7,8,9,0,1], 'i')
print(ARR1)

### Ther are 6 ways in which we can create an array using numpy

### 1 array()

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype) ### This we give us the type of array it is

arr1 = array([1,2,3,4,5.1])
print(arr1)  ### In an array we have to use only one type of variables , that is if one of the value is different python will convert the whole array into it
print(arr1.dtype) 

### we can also use (int) , (str) , (float) instead of using variables like i ,I , ect....
arr1 = array([1,2,3,4,5.1] , int)
print(arr1)  
print(arr1.dtype)

### 2 linspace()

arr2 = linspace(0,15,16)
print(arr2)
### linspace takes three arguments or parameters (start, stop, number of parts we want to dive it into)
arr3 = linspace(0,15)
print(arr3) ### By default , if we did not mention the divide parameter , it will get divided into 50 parts by default

### 3 arange()

arr4 = arange(0,15,2)
print(arr4)
### arange also takes three parameters (start ,stop , step)
### by default (step) is 1 when we are not mentioning anything

### 4 logspace()

arr5 = logspace(1,40,5)
print(arr5)
### this has a big relationn with log

### 5 zeros()

arr6 = zeros(10)
print(arr6)
### this will create an array of full of zeros according to the input or parameter we gave , in this case it is 10

### By default every value of zeros is in the form of float , to convert it we have to do the following

arr7 = zeros(10,int)
print(arr7)

### 6 ones()

arr8 = ones(10)
print(arr8)

### Every thing same for ones also

arr9 = ones(10,int)
print(arr9)
