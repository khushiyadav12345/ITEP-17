# 19. Mobile Phone Hierarchy
# Phone
# Smartphone
# AndroidPhone

# Add Android features.

class Phone:
    def calling(self):
        print("Phone can make calls")

class Smartphone(Phone):
    def internet(self):
        print("Smartphone supports internet")

class AndroidPhone(Smartphone):
    def androidFeature(self):
        print("Android phone supports Play Store")

a = AndroidPhone()

a.calling()
a.internet()
a.androidFeature()