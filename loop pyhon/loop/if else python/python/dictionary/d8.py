# 8. Frequency of Words in Sentence

# Count how many times each word appears.

# Example:

# sentence = "this is a test this is"

# 👉 Output:

# {'this': 2, 'is': 2, 'a': 1, 'test': 1}

sentence = "this is a test this is"
result = {}
for word in sentence.split():
    if word not in result:
        result[word] = 0
    result[word] += 1
    
print(result)

