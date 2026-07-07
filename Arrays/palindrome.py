def palindrome(string):
    rev = ''
    i = len(string)-1
    while i>= 0:
        rev = rev + string[i]
        i = i - 1
    if (rev == string):
        return "it is Palindrome"
    return "it is not a palindrome"
print(palindrome("madam"))