import random
class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name):
            self.name = name # each character should have its own name
            self.health = 120 # every hero has a harcoded 120hp
            self.attack_power = 25

    
    def attack(self):
            """Return a random amount of damage."""
            return random.randint(1,self.attack_power )
    
    def take_damage(self, damage):
            """Reduce health without allowing it to fall below zero."""
            self.health = self.health - damage
            if self.health < 0:
                   self.health = 0
    
    def is_alive(self):
            """Return True while the hero has health remaining."""
            return self.health > 0
