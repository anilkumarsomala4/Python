def String(stones,jewels):
    count = 0
    for ch in stones:
        if ch in jewels:
            count += 1
    return count
print(String("xxXYZ","xY"))