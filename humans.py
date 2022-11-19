#%%
import random
from player import Player
from creature import Creature
from items import Sword

class Human(Player):
   
    def __init__(self, name, x, y):
        super().__init__(name, x, y, 50)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'
        self.inventory = []


    def damage(self, object: Creature, sword: Sword):
        
        if self.has_sword(sword):
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

    def has_sword(self, sword: Sword) -> bool:
        
        for i in range(len(self.inventory)):
            if isinstance(self.inventory[i], type(sword)):
                return True
        return False

    def create_inventory(self, items):

        self.inventory += [items]
        return self.inventory


jugador1 = Human('facu', 10, 25)
espada = Sword("espadachin", chr(128481), 5, 10)
espada2 = Sword("espada", chr(128481), 5, 10)

jugador1.create_inventory(espada)
jugador1.create_inventory(espada2)

goblin = Creature((23, 10), 100)

d = jugador1.damage(goblin, espada)

print(espada.use_against(goblin, d))




# %%