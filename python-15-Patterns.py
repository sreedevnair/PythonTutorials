#########------------Ways to make HASH patterns---------############

print('# # # #')
print('# # # #')
print('# # # #')
print('# # # #')

print("")

### another way of doing this is

for i in range(4):
    print('# # # #')

print("")

### By only using one hash

for i in range(4):
    print("# ", end="")
print()
for i in range(4):
    print("# " , end="")
print()
for i in range(4):
    print("# " , end="")
print()
for i in range(4):
    print("# " , end="")
print()

print("")

### another method of doing this is

for i in range(4):
    for j in range(4):
        print("# ", end="")
        
    print()

print(" ")
### how to make other pattern also

a = 1
for i in range(4):
    for j in range(a):
        print("# ", end="")
    a = a+1
    print()

print(" ")

### Some more pattern 

b = 4
for i in range(4):
    for j in range(b):
        print("# ", end="")
    b= b-1    
    print()
        

