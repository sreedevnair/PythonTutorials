##########----------Fibonacci Sequence------------##############

def seq(x):
    i = 0
    j = 1
    print(i)
    print(j)


    if x < 1:
        print("invalid") 
    else:
        for a in range(0,x):
            c = i+j
            
            print(c)

            i = j
            j = c
    

seq(int(input("Enter the number for Fibonacci Sequence")))



