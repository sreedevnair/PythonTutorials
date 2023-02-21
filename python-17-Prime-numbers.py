x = int(input("Enter the number"))


for i in range(2 , x):
    if x%i==0:
        print("Its a composite number")
        break
    
else :
    print("Its a prime number")
