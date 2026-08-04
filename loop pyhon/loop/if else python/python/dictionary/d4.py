# 🔹 4. Find First Non-Repeating Character

# Use a dictionary to count frequency, then find first unique char.

# Example:

# text = "aabbcde"

# 👉 Output: c

text = "aabbcde"
result = {}
for char in text:
    result[char] = result.get(char, 0)+1

for key, value in result.items():
    if value == 1:
        print(key)
        break