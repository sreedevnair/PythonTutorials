######------Constructor , self and comparing object-------########

class computer:
    pass ### We are using pass because our computer class is empty

c = computer
print(id(c))



class computer2:
    def __init__(self):
        self.name = 'Sreedev'
        self.age = 14

c1 = computer2()
c2  = computer2()

print(c1.name)
print(c2.name)
### both will have the same name

c1.name = "Sreenath"
c1.age = 18

print(c1.name)
print(c1.age)

### in somthing.name() or in somthing.age() , (something) is passed in the closed brackets

### when we have to compare something

class computer3:
    
    def __init__(self):
        self.name = 'Sreedev'
        self.age = 14

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
            
c3 = computer3()
c4 = computer3()

c4.age = 18

if c3.compare(c4):
    print("They are same")
else:
    print("They are different")
