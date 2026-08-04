def numJewelsInStones(jewels, stones):
    count = 0
    for s in stones:
        if s in jewels:
            count += 1
    return count

print(numJewelsInStones("aAb", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))