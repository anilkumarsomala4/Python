def Secondlargest(nums):
    larget = 0
    Secondlargesst =0
    for i in nums:
        if i > larget:
            Secondlargesst =larget
            larget =i
        elif i > Secondlargesst and i != larget:
            Secondlargesst = i
    return Secondlargesst
print(Secondlargest([1,2,3,4,5,9]))