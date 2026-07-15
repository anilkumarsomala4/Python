def thirdlargest(nums):
    largest = 0
    secondlargest = 0
    thirdlargest = 0
    for i in range(len(nums)):
        ch = nums[i]
        if ch > largest:
            secondlargest = largest
            largest = ch
        elif ch < largest and ch > secondlargest:
            thirdlargest = secondlargest
            secondlargest=ch
        elif ch < secondlargest and ch > thirdlargest:
            thirdlargest = ch
    return thirdlargest
print(thirdlargest([99,20,29,30,40,68]))