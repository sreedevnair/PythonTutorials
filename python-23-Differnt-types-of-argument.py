#########------------Different tyoes of arguments in python----------------##########

def person(name,age): ### name an age are called formal arguments
    print(name)
    print(age)

person("sreedev" , 15) ### "sreedev" and 15 are called actual arguments

person(15 , "sreedev")
### This will print my name as 15 and my age as 'sreedev'

### To avoid this we have to use "keywords"

person(age=15,name="sreedev") ### In this case age and name are the keywords

print(" ")

########---------Default-------------###########

def name_age(name , age):
    print(name)
    print(age)

# name_age("sreedev") ### This will give us a error because of we only passed two arguments

def name_age(name , age=15): ### This will keep the default value of age as 15
    print(name)
    print(age)

name_age("sreedev") ### this will not throw any error because we have asssinged the value of age as 15

name_age("sreedev" , 22) ### but we can over write the default value

############------------variable length--------############

def sum1(*b):
    c = 0
    for i in b:
        c = c +1

    print(c)

sum(13,14,42,68,36)    
