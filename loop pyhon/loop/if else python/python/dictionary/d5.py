# 5. Two Sum Problem

# Given a list and a target, find indices of two numbers that add up to target.

# Example:

# nums = [2, 7, 11, 15]
# target = 9

# 👉 Output: [0, 1]

nums = [2,7,11,15]
target = 9
result = {}

for i in range(len(nums)):
 for j in range(i+1,len(nums)):
    if nums[i]+nums[j]==target:
        result[nums[i]]=i
        result[nums[j]]=j
print(list(result.values()))




