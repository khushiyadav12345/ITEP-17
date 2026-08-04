#  WAP to print Alphabets in reversing order.
N = int(input("Enter the number of terms: "))
for i in range(N):  
    print(chr(90 - i), end=" ")  # ASCII value of 'Z' is 90