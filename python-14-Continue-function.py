for x in range(1, 101):
    if x%3!=0 or x%5!=0:
        print(x)
### Doing in such a way , we must only use and , we cant use or

print(" ")

### we can do this in a seprate way

for a in range (1,101):
    if a%3==0 or a%5==0:
        continue
    print(a)
### in this case we cannot use and , we have to use or
