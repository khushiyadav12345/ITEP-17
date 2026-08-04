# 5) WAP to find out the factorial of a number.
N = int(input("Enter a number:"))
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
print("The factorial of", N, "is:", factorial)