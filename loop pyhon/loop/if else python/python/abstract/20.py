# 20. Gaming Characters
# Character
# Warrior
# SuperWarrior

# Add special powers.

class Character:
    def attack(self):
        print("Character is attacking")

class Warrior(Character):
    def weapon(self):
        print("Warrior uses a sword")

class SuperWarrior(Warrior):
    def specialPower(self):
        print("Super Warrior has fire power")

s = SuperWarrior()

s.attack()
s.weapon()
s.specialPower()