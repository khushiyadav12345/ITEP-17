# 14. Multiple Inheritance Example

# Classes:

# Father
# Mother
# Child(Father, Mother)

# Access methods from both.

class Father:
    pass
class Mother:
    pass
class Child(Father, Mother):
    pass
c = Child()
print(c)

