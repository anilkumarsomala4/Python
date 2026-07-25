n = 10
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j>n/2):
            print("* ",end="")
        else:
            print("  ",end="")
    print()    