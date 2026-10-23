def Roman(nums):
    values = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
    sum = 0
    num = len(nums)
    for i in range(num):
        temp = values[nums[i]]
        if i+1 < num and temp < values[nums[i+1]]:
            sum = sum - temp
        else:
            sum = sum + temp
    return sum
print(Roman("DCCXCVI"))