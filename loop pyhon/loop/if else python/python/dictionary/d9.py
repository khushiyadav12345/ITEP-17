# 9. Find Common Keys in Two Dictionaries

# Return keys present in both.

# Example:

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# 👉 Output: ['b']

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = {}
for key in d1:
    if key in d2:
        result[key] = d1[key]
print(list(result.keys()))