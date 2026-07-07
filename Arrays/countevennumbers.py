def countevennumber(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1
    return count
print(countevennumber([2, 5, 8, 11, 14, 17]))