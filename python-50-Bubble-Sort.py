#########-------Bubble Sort-------###########

def sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                j = j+1
                            
nums = [5,3,8,6,7,2]

sort(nums)

print(nums)

print(len(nums))



