#  WAP to check whether entered number is strong or not
N = int(input("Enter a number: "))
factorial = 1
temp = N
sum_of_factorials = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    temp //= 10
if sum_of_factorials == N:
    print("The number is a strong number.")
else:
    print("The number is not a strong number.")
    
    