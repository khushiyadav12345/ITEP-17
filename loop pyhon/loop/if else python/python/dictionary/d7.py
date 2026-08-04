#  7. Check Anagram Using Dictionary

# Check if two strings are anagrams using character count.

# Example:

# s1 = "listen"
# s2 = "silent"

# 👉 Output: True

s1 = "listen"
s2 = "silent"

count1 = {}
count2 = {}

for ch in s1:
    count1[ch] = count1.get(ch, 0) + 1

for ch in s2:
    count2[ch] = count2.get(ch, 0) + 1

if count1 == count2:
    print(True)
else:
    print(False)