##########--------Duck Typing-----------###########

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")
 
class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Conventional Check")
        print("Compiling")
        print("Running")
 
class laptop:

    def code(self,ide):
        ide.execute()
        
ide = PyCharm() ### In python we can do dynamic programming which means variables are mutable
### we can cgange the value of the ide above mentioned

lap1 = laptop()
lap1.code(ide)

ide = MyEditor()

lap1 = laptop()
lap1.code(ide)

### This is called Duck Typing
