def vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count = count + 1
    print(count)
vowels("Hello")      


