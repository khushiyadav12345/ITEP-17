# 13) WAP to print N natural numbers in reverse order
N = int(input("Enter a number: "))
print("Natural numbers in reverse order:")
for i in range(N, 0, -1):
    print(i, end=" ")