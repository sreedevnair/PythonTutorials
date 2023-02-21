#######--------Factorial usng recursion--------#########

def fact(n):

    if n==0:
        return 1
    return n*fact(n-1) ### Recurnsion is happening here

print(fact(0))

