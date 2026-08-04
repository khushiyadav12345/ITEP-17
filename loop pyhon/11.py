# 11) WAP to print N odd numbers.
N = int(input("Enter a number: "))
print("First", N, "odd numbers are:")
for i in range(1, 2 * N, 2):
    print(i, end=" ")