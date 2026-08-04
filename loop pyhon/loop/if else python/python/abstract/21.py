# 21. Shape Area Calculator

# Abstract class Shape.

# Derived:

# Circle
# Rectangle
# Triangle

# Implement area calculation.



# its wrong
class Area:
    def __init__(self,c,r):
      self.__c = c
      self.__r = r

    def getarea(self):
        return self.__c * self.__r
    
class Volume(Area):
    def __init__(self,c,w,h):
        super().__init__(c,w)
        self.__h = h

    def getvolume(self):
        return self.getarea() * self.__h    

class Density(Volume):
    def __init__(self,c,w,h,m):
        super().__init__(c,w,h)
        self.__m = m

    def getdensity(self):
        return self.__m/self.getvolume()    

d = Density(2,3,4,100)

print(f"Area : {d.getarea()}")
print(f"Volume : {d.getvolume()}")
print(f"Density : {d.getdensity():.2f}")