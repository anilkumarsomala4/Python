def Zpattern(num):
    if num % 2 != 0:
        num = num + 1
    for i in range(1,num):
        for j in range(1,num):
            if i == 1 or i == 5 or i+j == num:
                print("* ",end="")
            else:
                print("  ",end="")
        print()
Zpattern(5)