def Revrse(nums):
    low = 0
    high = len(nums)-1
    while(low<high):
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp
        low=low+1
        high = high-1
    return nums
print(Revrse([1,2,3,4,5]))