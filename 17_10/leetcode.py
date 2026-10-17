# 2016. Maximum Difference Between Increasing Elements
def Maximum(nums):
    ans = -1
    low = nums[0]
    for i in range(1,len(nums)):
        if low < nums[i]:
            temp = nums[i] - low
            ans = max(temp,ans)
        low = min(low,nums[i])
    return ans
print(Maximum([7,1,5,4]))