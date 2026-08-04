# 27) *	#	*	#	*	#	*	#	*	…….
N = int(input("Enter the number of terms: "))
for i in range(N):
    if i % 2 == 0:
        print("*", end=" ")
    else:
        print("#", end=" ")