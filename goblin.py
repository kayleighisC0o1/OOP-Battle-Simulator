import random
from enemy import Enemy


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 100, attackPower=15)
        self.attack_power = 15

    def stealGold(self, hero):
        """Return a random amount of damage."""
        self.gold = 0
        self.gold += hero.gold
        hero.gold = 0
        print("GET REKT NOOB")

