def sum(num):
    sum = 0
    if num < 1:
        return
    while (num > 0):
        digit = num % 10
        sum = sum + digit
        num = num // 10
    print(sum)
sum(123)