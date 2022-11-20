#%%
from typing import Union

from creature import Creature
import random

numeric = Union[float, int]


class Item:
    def __init__(self, name, fc, type):
        self.name = name
        self.face = fc
        self.type = type

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"

class Sword(Item):
    def __init__(self, name: str, fc: str, min_dmg: numeric, max_dmg: numeric):
        super().__init__(name, fc, 'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        
    def use_against(self, object: Creature, dmg: numeric) -> numeric:
        
        while object.health > 0:
            object.health -= dmg
            
        return object.health

#espada1 = Sword("espadachin", chr(1232), 5, 10)

#goblin = Creature((2,3), 100)

#print(espada1.use_against(goblin, 10))

#%%
class Box(Item):
    def __init__(self, name: str, fc: str, min_dmg: numeric, max_dmg: numeric):
        super().__init__(name, fc, 'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
      
class PickAxe(Item):
    def __init__(self, name: str, fc: str, dmg: numeric, n_hits: numeric):
        super().__init__(name, fc, 'tool')
        self.fc = chr(9935)

    def use_against(self, object):
        pass

class Potion(Item):
    def __init__(self, name: str, fc: str):
        super().__init__(name, fc, "consumable")

class Amulet(Item):
    def __init__(self, name: str, fc: str): #chr(127873), chr(127988)
        super().__init__(name, fc, 'treasure')

