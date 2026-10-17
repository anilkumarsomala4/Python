def Missingnumber(nums):
    sum = 0
    num = len(nums)
    for i in range(1,num+2):
        sum = sum + i
    arr_sum = 0
    for i in nums:
        arr_sum = arr_sum + i
        res = sum - arr_sum
    return res
print(Missingnumber([1,2,3,5,6,7,8]))