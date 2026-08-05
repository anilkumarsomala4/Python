num = 10
if num % 2 != 0:
    num = num + 1
for i in range(1,num):
    for j in range(1,num):
        if(i==num-1 or j==num/2 or j+i == num / 2):
            print("* ",end="")
        else:
            print("  ",end="")
    print()