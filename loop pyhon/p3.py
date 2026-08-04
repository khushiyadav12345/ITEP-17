# 3) WAP to find out the sum of N natural number.
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N + 1):
    sum = i + sum
print("The sum of first", N, "natural numbers is:", sum)