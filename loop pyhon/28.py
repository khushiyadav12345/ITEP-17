# 28) 1	2	3	4	 Hello	6	7	8	9	Hello	11	12 ….
N = int(input("Enter the number of terms: "))
for i in range(1, N + 1):
    if i % 5 == 0:
        print("Hello", end=" ")
    else:
        print(i, end=" ")