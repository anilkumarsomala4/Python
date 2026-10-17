def Secondsmallest(nums):
    smallest = float('inf')
    Secondsmallest = float('inf')
    for i in nums:
        if i < smallest:
            Secondsmallest = smallest
            smallest = i
        elif i <Secondsmallest and i != smallest:
            Secondsmallest = i
    return Secondsmallest
print(Secondsmallest([10, 20, 4, 45, 99, 4, 2]))