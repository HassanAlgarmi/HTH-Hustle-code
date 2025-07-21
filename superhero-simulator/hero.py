
import random
from abillity import Ability
from armour import armour
class Hero:

    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armour = []

    def battle(self, opponent):
        self.opponent = opponent
        winner = random.choice([self.name, opponent])
        print(f"{winner}")
    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armour(self, armour):
        self.armour.append(armour)
    
    
    def sum_of_attack(self):
     total_damage = 0  
     for ability in self.abilities:
         total_damage += ability.attack()
         return total_damage


    def sum_of_block(self):
      total_block = 0 
      for armour in self.armour:
         total_block += armour.block()
         return total_block
    
if __name__ == "__main__":
    my_hero = Hero("one punch man", 200000000000)
    print(my_hero.name)            
    print(my_hero.current_health)  


