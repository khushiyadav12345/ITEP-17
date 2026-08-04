# 7️⃣ Leap Year Check

# Write a JavaScript program using the conditional operator to check whether a given year is a leap year.

year = 2026
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = f"{year} is a leap year."
        else:
            result = f"{year} is not a leap year."
    else:
        result = f"{year} is a leap year."
else:
    result = f"{year} is not a leap year."
print(result)