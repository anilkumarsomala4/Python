def Twosum(list):
    target = 8
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            anil = list[i] + list[j]
            if(anil == target):
                return i,j
print(Twosum([2,3,5,6,7]))

    