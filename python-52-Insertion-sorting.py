#######---------Insertion Sorting------------########

def insertion_sort(A):

    for i in range(1 , len(A)):
        for j in range(i-1,0,-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1] , A[j]
            else:
                break
    return A
list = [3,5,4,7,7,7,77,4,5,3]

print(insertion_sort(list))
