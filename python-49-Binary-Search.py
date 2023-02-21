
########--------Binary Search--------##########

pos = "something"

def search(list,n):

    l = 0
    u = len(list)-1### we are subtracting one beacuse the len fuction start's the index value from 1

    while l <= u:
        mid = int((l+u)/2)

        if list[mid] == n :
           globals() ['pos'] = mid
           return True
        else :
            if list[mid] < n:
                l = mid+1 ### we are adding one beacuse of the len function

            else:
                u = mid-1 ### Same as the above
                
    return False 

list = [1,3,5,7,8,12,15,16]

n = 3

if search(list , n):
    print('valuse found at' , pos)
else:
    print('valuse not found')
