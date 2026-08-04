# WAP to check whether entered number is perfect or not
N = int(input("Enter a number:"))
sum_of_divisors = 0
for i in range(1, N):
    if N % i == 0:
        sum_of_divisors += i

if sum_of_divisors == N:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")    