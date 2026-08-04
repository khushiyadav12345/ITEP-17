# 30. Restaurant Management

# Abstract:

# Restaurant

# Derived:

# PizzaRestaurant
# BurgerRestaurant

# Prepare food differently.

from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def prepareFood(self):
        pass


class PizzaRestaurant(Restaurant):
    def prepareFood(self):
        print("Preparing Pizza")


class BurgerRestaurant(Restaurant):
    def prepareFood(self):
        print("Preparing Burger")


p = PizzaRestaurant()
p.prepareFood()

b = BurgerRestaurant()
b.prepareFood()