"""
Starbuzz coffee

Author: m1ge7 and Eric Wang
Date: 2018/09/02
"""

from abc import ABCMeta, abstractmethod

menu = {
    # Beverages
    'HouseBlend': 0.89,
    'DarkRoast': 0.99,
    'Espresso': 1.99,
    'Decaf': 1.05,
    # Add-ons
    'Milk': 0.10,
    'Mocha': 0.20,
    'Soy': 0.15,
    'Whip': 0.10
}

###############################################################################
# Beverages
###############################################################################

class Beverage:
    """The abstract class constructing beverages and the CondimentDecorator."""
    __metaclass__ = ABCMeta

    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return menu['HouseBlend']


class DarkRoast(Beverage):

    def __init__(self):
        self._description = "Dark Roast Coffee"

    def cost(self):
        return menu['DarkRoast']


class Espresso(Beverage):

    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return menu['Espresso']


class Decaf(Beverage):

    def __init__(self):
        self._description = "Decaf Coffee"

    def cost(self):
        return menu['Decaf']


###############################################################################
# Condiment decorators
###############################################################################

class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_description(self):
        pass


class Milk(CondimentDecorator):

    def __init__(self, input_beverage):
        self._beverage = input_beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return menu['Milk'] + self._beverage.cost()


class Mocha(CondimentDecorator):

    def __init__(self, input_beverage):
        self._beverage = input_beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self):
        return menu['Mocha'] + self._beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, input_beverage):
        self._beverage = input_beverage

    def get_description(self):
        return self._beverage.get_description() + ", Soy"

    def cost(self):
        return menu['Soy'] + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, input_beverage):
        self._beverage = input_beverage

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

    def cost(self):
        return menu['Whip'] + self._beverage.cost()


###############################################################################
# Simulation
###############################################################################

if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))
