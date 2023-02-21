######-----Inheritance------#######

class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A): ###Using bracket , weare saying that class (B) is a child or sub class of class A and will inheritance all the properties from class A
    def feature3(self):
        print("feature 3 is working")
    ### This is called single level inheritance
        
    def feature4(self):
        print("feature 4 is working")

class C(B): ### this will get what B and A have because B also have what A have 
    def feature5(self):
        print("feature 5 is working")
    ### This is called multi level inheritance
        
a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()

c1 = C()
c1.feature2()


### Aother type of inheritence is

class E:
    def feature6(self):
        print("feature 6 is working")

    def feature7(self):
        print("feature 7 is working")

class F(): 
    def feature8(self):
        print("feature 8 is working")
        
    def feature9(self):
        print("feature 9 is working")

class H(E,F):
    def feature0(self):
        print("feature 0 is working")
    ### This will get the all property of class E and F

h1 = H()
h1.feature7()
        
