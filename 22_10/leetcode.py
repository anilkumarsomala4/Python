# 1299. Replace Elements with Greatest Element on Right Side 
# solving in o(n)
def greater(arr):
    ans = -1
    for i in range(len(arr)-1,-1,-1):
        temp = arr[i]
        arr[i] = ans
        ans = max(ans, temp)
    return arr
print(greater([7,6,5,4,3,2,0]))