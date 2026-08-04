# 8) WAP to print Fibonacci series.
N = int(input("Enter a number:"))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b