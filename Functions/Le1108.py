def anil(s):
    ans = ""
    for i in s:
        ch = i
        if ch == ".":
            ans = ans + "[.]"
        else:
            ans = ans + ch
    return ans
print(anil("1.1.1.1"))
