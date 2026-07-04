def anil(s):
    ans = ""
    for i in s:
        if i == ".":
            ans = ans + "[.]"
        else:
            ans = ans + i
    return ans
print(anil("1.1.1.1"))
