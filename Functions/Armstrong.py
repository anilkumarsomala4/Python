def strong(num):
    count = 0
    sum = 0
    total = 0
    org = num
    temp = num
    if num < 0:
        return 
    while(num > 0):
        count = count + 1
        num = num // 10
    while(org > 0):
        digit = org % 10
        sum = digit ** count
        total = total + sum
        org = org // 10
    if (temp == total):
        print("Yes it is Arm Strong number")
    else:
        print("No It's not Arm Strong number")    
strong(153)
