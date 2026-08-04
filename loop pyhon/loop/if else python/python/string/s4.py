# def length_of_last_word(s):
#     i = len(s)-1
#     counter = 0
    
#     while s[i] == " ":
#         i-=1
    
#     while s[i]!=" ":
#         counter += 1
#         i -= 1
#     return counter;

# result = length_of_last_word(" HelloWorld")
# print(f"{result}")





class A:
    successcode = 200
    def __init__(self):
        self.error = 404
        
class B(A):
    def displaycode(self):
        print(self.error)
        print(self.successcode)
        print(super().successcode)
        print(super().error)
        
obj = B()
obj.displaycode()