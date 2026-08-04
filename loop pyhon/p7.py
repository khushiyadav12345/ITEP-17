# 7) WAP to check whether entered number is prime or not.
N = int(input("Enter a number:"))
is_prime = True
for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break
if is_prime:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")
   
