def strong(num):
    org = num
    sum = 0
    while(num > 0):
        fact = 1
        digit = num % 10
        for i in range(1,digit+1):
            fact = fact * i
        sum = sum + fact
        num = num // 10
    if (sum == org):
        return "Yes it is a Strong Number"
    return "No it is not a Strong Number"
print(strong(2))

