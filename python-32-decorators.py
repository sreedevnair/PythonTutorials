##############-----------Decorators-----------##############

### Using decorators we can add extra features in a existing function

def div(a,b):
    print(a/b)

### When we have to divide the bigger number with a smaller number , we have to do the following
    
def smart_div(func):
    
    def inner(c,d):
        if c<d:
            c,d = d,c
        return func(c,d)
    return inner

div1 = smart_div(div)

div1(2,10)
