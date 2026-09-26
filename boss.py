import random
from enemy import Enemy


class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=200, attackPower=25)

    def attack(self):
        attackStyle = random.randint(1,3)
        if attackStyle == 1:
            print("PUNCH")
            return 5 * random.randint(1,3)
        elif attackStyle == 2:
            print("attack jump")
            return self.attack_power
        else:
            print("BOOM")
            return 2 * random.randint(2,6)
    def take_damage(self, damage):
        damage = damage * .75
        super().take_damage(damage)