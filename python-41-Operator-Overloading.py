##########---------Opertor Overloading-----------############

a = 5
b = 5

print(a + b)

### another method of doing such things are

print(int.__add__(a,b))

### Same we have to do for string also

c = "Hello "
d = "World"

print(c + d)

print(str.__add__(c,d))

### For addition we are using __add__() , for subtraction we are using __sub__() , and for multiplication __mul__()

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)

        return s3

s1 = student(58,69)
s2 = student(60,65)

s3 = s1 + s2

print(s3.m1)

### we can also do such thungs by using __sub__() , __mul__()
