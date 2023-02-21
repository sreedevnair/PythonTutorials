#######------Object Orianted Programming--------########

### The Class in OOP means the bluprint or the design of an object
### The Object in OOP means the product which was designed using the class

### Class have two things , Attributes which means Variables and Behaviour which means Methods[Function]

class computer:



    def features(self):
        print("i3 , 6gb ,1TB")
### (self)is the name of the object we have to mention in this class
        
com1 = computer()
### com1 is refering to the self input
print(type(com1))

computer.features(com1)
### If we have to use the function inside a class we have to do the above things , not like normal function

### Adding more marks :-

com2 = computer()

computer.features(com2)

### We will be getting the same output becomes we have only one data , we can have more than one data in an class

com1.features() ### we can also do this , this way

com2.features()
