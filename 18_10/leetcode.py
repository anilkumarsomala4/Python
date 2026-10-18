# 2078. Two Furthest Houses With Different Colors
# solving in o(n)*2
def maxm(nums):
    ans = 0
    num = len(nums)
    for i in range(num):
        for j in range(i+1,num):
            if nums[i] != nums[j]:
                temp = j - i
                ans = max(temp, ans)
    return ans
print(maxm([4,4,4,11,4,4,11,4,4,4,4,4]))