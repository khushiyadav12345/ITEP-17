class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec

    def __add__(self,other):
        temp=Time(0,0,0)
        temp.hr=self.hr+other.hr
        temp.min=self.min+other.min
        temp.sec=self.sec+other.sec

        if temp.sec>=60:
            temp.min+=1
            temp.sec-=60
        if temp.min>=60:
            temp.hr+=1
            temp.min-=60
        return temp
    
    def __str__(self):
        return f"{self.hr} hour {self.min} min {self.sec} sec"
    
obj1=Time(2,30,59)
obj2=Time(2,30,11)
obj3=obj1+obj2
print(obj3)