# 6️⃣ Grade Calculation

# Write a program using the conditional operator to assign grades based on marks:

# ≥ 90 → A

# ≥ 75 → B

# ≥ 60 → C

# < 60 → Fail

marks = 59
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
print(f"Grade: {grade}")