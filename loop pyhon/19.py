# 19) 1	+	1/2	+	1/3	+	1/4	+	1/5	….. n terms(find out sum)
n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print("The sum of the series is:", sum)
    



    