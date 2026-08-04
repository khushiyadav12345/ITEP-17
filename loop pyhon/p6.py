# 6) WAP to find out the factors of a number.
N = int(input("Enter a number:"))
print("The factors of", N, "are:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)