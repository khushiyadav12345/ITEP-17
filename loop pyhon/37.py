# WAP to check whether entered number is palindrome or not 
N = int(input("Enter a number: "))
original_number = N
reverse = 0
while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N = N // 10
if original_number == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    