# 16) …... -6	-3	0	3	6	9	……. n terms [where n is even number]
N = int(input("Enter the number of terms to print (even number): "))
if N % 2 != 0:
    print("Please enter an even number.")
    print("Exiting the program.")
else:
    for i in range(N):
        term = -6 + 3 * i
        print(term, end="\t")

