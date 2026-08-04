# 12) WAP to print Odd numbers upto N.
N = int(input("Enter a number: "))
print("Odd numbers upto", N, "are:")
for i in range(1, N + 1, 2):
    print(i, end=" ")
    