def factorial(num):
    fact = 1
    if num == 0 and num == 1:
        return 1
    while num > 1:
        fact = fact * num
        num = num -1
    print(fact)
factorial(5)