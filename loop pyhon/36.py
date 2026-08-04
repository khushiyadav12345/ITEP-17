#  WAP to reverse a number
N = int(input("Enter a number: "))
reverse = 0
while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N = N // 10
print("Reversed number:", reverse)
    