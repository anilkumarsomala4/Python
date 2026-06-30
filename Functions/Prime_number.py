def Prime_number(num):
    if num <= 1:
        return "It is Not a Prime Number"
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if (count == 2):
        return f"Yes {num} is a Prime Number"
    else:
        return f"No {num} is Not a Prime Number"
prime = Prime_number(8)
print(prime)