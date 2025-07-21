import random


class armour:
    def __init__(self, name, max_block):
   	# implement code here
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a random value between 0 and max_block'''
	# implement code here
        return random.randint(0, self.max_block)

if __name__ == "__main__":
    super_armour = armour("serious block", 500000000000000000000000000000000000000000000000000)
    print(super_armour.block())