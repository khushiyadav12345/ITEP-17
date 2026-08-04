# 23) 1	9	25	49	81	…..
N = int(input("Enter the number of terms: "))
for i in range(1, N + 1):
    print(i * i * i, end=" ")