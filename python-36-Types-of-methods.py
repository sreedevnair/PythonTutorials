######-----Types of methods------######

### There are 3 types of methods. Class method , Instance method and static method

class student:

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): ### this is an instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls): 
        return cls.school
    ### As school is a class variable , we have to use the cls instead of self which we use in a instance variable

    @staticmethod
    def info():
        print("This is a static method")
    
s1 = student(34,53,37)
s2 = student(74,65,12)

print(s1.avg())

print(s1.getschool())

### To do the same thing in an another way we have to mention @classmethod at the first , then we have to do the following
print(student.getschool())

student.info()
