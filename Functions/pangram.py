def string(sentence):
    sentence.lower()
    dict = {}
    for ch in sentence:
        if ch >= "a" and ch <= "z":
            dict[ch] = 0
    if(len(sentence)==26):
        return True
    return False
print(string("Anil"))
