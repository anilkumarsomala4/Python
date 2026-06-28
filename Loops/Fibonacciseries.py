num = int(input("Enter digit to get series: "))
a = 0
b = 1
count = 0
while(count < num):
    print(a,end=" ")
    c = a+b
    a=b
    b=c
    count = count + 1
    print()