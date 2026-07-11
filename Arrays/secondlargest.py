def secondlargest(nums):
    largest = 0
    secondlargest = nums[0]
    for i in range(len(nums)):
        ch = nums[i]
        if ch > largest:
            secondlargest = largest
            largest = ch
    return secondlargest
print(secondlargest([10, 25, 8, 40, 15]))