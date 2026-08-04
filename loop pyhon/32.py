# A	b	C	d	E	f	G	h	…… n terms  
N = int(input("Enter the number of terms: "))
for i in range(N):
    if i % 2 == 0:
        print(chr(65 + i), end=" ")  # Uppercase letters (A, C, E, ...)
    else:
        print(chr(97 + i), end=" ")  # Lowercase letters (b, d, f, ...)