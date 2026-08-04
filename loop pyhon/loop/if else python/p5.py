# 5️⃣ Maximum of Three Numbers

# Write a JavaScript program using nested ternary operators to find the maximum of three numbers.
number1 = 10
number2 = 20
number3 = 150
if number1 >= number2 and number1 >= number3:
    result = f"{number1} is the largest number."
elif number2 >= number1 and number2 >= number3:
    result = f"{number2} is the largest number."
else:
    result = f"{number3} is the largest number."
print(result)