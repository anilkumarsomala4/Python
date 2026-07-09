def anil(nums,k):
    sum = 0
    for i in nums:
        sum = sum + i
    if sum == k:
        return 0
    return sum % k
print(anil([3,9,7],5))
