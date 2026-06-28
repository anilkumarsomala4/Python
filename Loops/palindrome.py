num = int(input("Enter a number: "))
rev = 0
org = num
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if(rev == org):
    print("Yes it is palindrome")
else:
    print("No it's not palindrome")