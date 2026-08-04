# 18) 1	2	2	4	8	32	…… n terms
N = int(input("Enter the number of terms to print: "))
term = 1
print(term, end="\t")
for i in range(1, N):
    term *= 2
    print(term, end="\t")

