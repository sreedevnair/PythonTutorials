#########-----Constructor in inheritance------#####

class A:

    def __init__(self):
        print("in A init")
        
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):

    def __init__(self):
        super().__init__() ### this will print the init from class a also
        print("in B init")
    ### If you create object of sub class it will first try to find init of the sub class , if not found then it will call init of the super class


    ### What is happening is that in __init__ method it will first print the init from the super class as we have mentined and then it will print the init of class B
    def feature3(self):
        print("feature 3 is working")
        
    def feature4(self):
        print("feature 4 is working")

b1 = B()


