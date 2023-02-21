#######-------Types of varaibles in OOP---------#######

### There are two types of variables in OOP that are , Instant and Class Variable

class car:

    wheels = 4
    ### this is a class variable because it can by changed together

    def __init__(self):
        self.mil = 10 ### Mileage
        self.com = "BMW" ### Company
        ### the above is is an Instance variable
        
c1 = car()
c2 = car()

print(c1.mil , c1.com)
print(c2.mil , c2.com)

c2.mil = 8
c2.com = "SWIFT"

print(c1.mil , c1.com , c1.wheels)
print(c2.mil , c2.com , c2.wheels)

car.wheels = 2

print(c1.mil , c1.com , c1.wheels)
print(c2.mil , c2.com , c2.wheels)
