#######-------Method overloading and method overriding--------#######

### Method Overloading
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None): ### using none we can types nothing in the input if not needed

        s = 0

        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
            

        return s

s1 = student(59,69)

print(s1.sum(2,6))

### Method Overriding

class A:

    def show(self):
        print("in A show")

class B(A):

    def show(self):
        print("in B show") ### If the inheriteded class have the same function  , it will print its own function 

a1 = A()
a1.show()

b1 = B()
b1.show()
