# 2078. Two Furthest Houses With Different Colors
# solving in o(n)
def maxm(nums):
    ans = 0
    for i in range(len(nums)):
        if nums[0] != nums[i]:
            temp = i
            ans = max(temp, ans)
    for i in range(len(nums)-1,-1,-1):
        if nums[i] != nums[len(nums)-1]:
            temp = (len(nums)-1)-i
            ans = max(temp,ans)
    return ans
print(maxm([4,4,4,11,4,4,11,4,4,4,4,4]))
