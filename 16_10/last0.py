def Last(nums):
    num = 0
    for i in nums:
        if i != 0:
            nums[num] = i
            num = num + 1
    for i in range(num,len(nums)):
        nums[i] = 0
    return nums
print(Last([1,0,2,3,0,4]))