# ability.py
import random

class Ability:
    def __init__(self, name, max_damage):
   	# implement code here
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and max_damage'''
	# implement code here
        return random.randint(0, self.max_damage)


# testing!
if __name__ == "__main__":
    fireball = Ability("serious punch", 500000000000000000000000000000000000000000000000000)
    print(fireball.attack())
