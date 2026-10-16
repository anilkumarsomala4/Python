def Best(nums):
    min = nums[0]
    max = 0
    for i in nums:
        if i < min:
            min = i
        profit = i - min
        if profit > max:
            max = profit
    return max
print(Best([7,2,1,4,7,3,8]))