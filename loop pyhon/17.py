# 17) 1 	2	 4	 7	 11	 16 	…… n terms
N = int(input("Enter the number of terms to print: "))
for i in range(N):
    term = (i * (i + 1)) // 2 + 1
    print(term, end="\t")
    

