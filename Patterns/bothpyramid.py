n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end="")
    for k in range(2*i-1):
        print("* ",end="")
    print()
for i in range(1,n+1):    
    for l in range(i-1):
        print("  ",end="")
    for m in range(2*n - 2*i+1):
        print("* ",end="")
    print()