def arr(list):
    x=0
    for i in (list):
        if(i== "X++" or i == "++X"):
            x = x+1
        elif(i=="X--" or i == "--X"):
            x=x-1
    return x
print(arr(["--X","X++","X++"]))