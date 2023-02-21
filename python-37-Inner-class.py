

class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
        
    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.ram = 8

        def show(self):
            print(self.brand , self.ram)
        
s1 = student('Sreedev',2)
s2 = student('Sreenath',5)

s1.name

s1.show()

