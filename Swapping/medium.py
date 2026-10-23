def Swapping(nums):
    num = len(nums)
    for i in range(0,num-1,2):
        temp = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp
    return nums
print(Swapping([1,2,3,4,5,6]))
            