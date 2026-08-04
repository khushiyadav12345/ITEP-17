# #  Find Most Frequent Vowel and Consonant
# vowels = "aeiaeia"
# vowel_max = 0
# consonant_max = 0 
# for char in vowels:
#             if char in vowels:
#                 vowel_max = max(vowel_max, vowels.count(char))
        
# for char in vowels:
#             if char not in vowels:
#                 consonant_max = max(consonant_max, vowels.count(char))
                
# print(f"Most Frequent Vowel Count: {vowel_max}")
# print(f"Most Frequent Consonant Count: {consonant_max}")







class A:
    def __init__(self):
        pass
    def wish(self):
        pass
    @classmethod
    def m1(cls):
        pass
    def m2():                            
        pass
    
class B(A):
    def __init__(self):
            super().__init__()
            super().wish()
            super().m1()
            super().m2()
            
    @classmethod
    def m1(cls):
        super().m1()
        super().m2()
        super(B,cls).wish(cls)
        super(B,cls).__init__(cls)
        
    @staticmethod
    def m2():
        super(B,B).m1()
        super(B,B).wish(B)
            
        