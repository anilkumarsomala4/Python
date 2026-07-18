n=6
for i in range(1,n):
    for j in range(1,n):
        if (i == 1 and j == 3) or (i == 2 and (j == 2 or j == 4)) or (i == 3 and (j ==1 or j == 5)):
            print(" *",end="")
        elif (i == 4 and (j ==1 or j == 5)) or (i == 5 and (j ==1 or j == 5)):
            print(" *",end="")
        elif(i == 3 and j == 3):
            print("*",end="")
        else:
            print(" ",end="")
    print("   ",end="")
    for j in range(1,n):
        if(j == i) or (j == 1) or (j==5):
            print(" *",end="")
        else:
            print(" ",end="")
    print("  ",end="")
    
    for j in range(1,n):
        if(j == 2):
            print(" *",end="")
        else:
            print(" ",end="")
    print(" ",end="")
    
    for j in range(1,n):
        if(j == 1) or (i == 5):
            print(" *",end="")
        else:
            print(" ",end="")
    print()



