def Xpattern(num):
    if num % 2 != 0:
        num = num + 1
    for i in range(1,num):
        for j in range(1,num):
            if (i == j) or (j+i == num):
                print("* ",end="")
            else:
                print("  ",end="")
        print()
Xpattern(15)