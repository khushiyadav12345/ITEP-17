#  WAP to count no. Of even and odd digits in a number
N = int(input("Enter a number: "))
even_count = 0
odd_count = 0
while N > 0:
    digit = N % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    N = N // 10
print("Number of even digits:", even_count)
print("Number of odd digits:", odd_count)
