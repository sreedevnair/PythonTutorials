########--------Factorial in python---------########


def fact(n):
    k = 1
    for i in range(1,n+1):
        k = i*k
    print(k)

fact(int(input("Enter the value")))



