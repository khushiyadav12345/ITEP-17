# 38) WAP to check whether entered number is Armstrong or not
N = int(input("Enter a number: "))
original_number = N
num_digits = len(str(N))
armstrong_sum = 0
while N > 0:
    digit = N % 10
    armstrong_sum += digit ** num_digits
    N = N // 10
if original_number == armstrong_sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
    