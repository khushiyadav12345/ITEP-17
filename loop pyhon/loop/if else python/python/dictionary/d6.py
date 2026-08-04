# 6. Sort Dictionary by Value

# Sort dictionary in ascending order of values.

# Example:

# data = {"a": 3, "b": 1, "c": 2}

# 👉 Output:

# {'b': 1, 'c': 2, 'a': 3}

data = {"a": 3, "b": 1, "c": 2}
l = list(data.items())
for i in range (len(l)):
    for j in range(i+1,len(l)):
        if l[i][1]>l[j][1]:
            l[i],l[j]=l[j],l[i]
print(f"Result: {dict(l)}")