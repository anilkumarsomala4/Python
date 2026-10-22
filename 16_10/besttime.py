def Best(nums):
    min = nums[0]
    max = -1
    for i in range(1,len(nums)):
        if nums[i] < min:
            min = nums[i]
        profit = nums[i] - min
        if profit > max:
            max = profit
    return max
print(Best([1,9,4,3,2]))