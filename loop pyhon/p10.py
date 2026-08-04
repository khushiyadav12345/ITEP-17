# 10) WAP to print Even numbers upto N.
N = int(input("Enter a number: "))
print("Even numbers upto", N, "are:")
for i in range(2, N + 1, 2):
    print(i, end=" ")