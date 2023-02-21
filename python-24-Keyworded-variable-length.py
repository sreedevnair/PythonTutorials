#####-----Keyworded variable length-----#####

def person(name, *data):
    print(name)
    print(data)

person("sreedev", "Mumbai" , 15)
### here name is refering to sreedev and data is refering to Mumbau , 15

def person(name, *data):
    print(name)
    print(data)

#print("sreedev",address="Mumbai",age=15)

### To use keywords , we have to mention **

def person(name, **data):
    print(name)
    print(data)

person("sreedev", address="Mumbai", age=15)

### We can also use for loop for this

def person(name, **data):
    print(name)
    
    for i,j in data.items(): ### we have to use .item while using for loop in this case
        print(i,j)

person("sreedev", address="Mumbai", age=15)

