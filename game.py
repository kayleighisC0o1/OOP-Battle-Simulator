from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Bumble clot"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive:
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("BeeWasiner")
    print("The gates are opening...")

    goblin = Goblin("Branch")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    hero = Hero("Fredwake")

    print(f"{hero.name} is in the HIZZOUSE with {hero.health} health")
    print(f"HE IS COOKING UP SOME GOBLIN SOUPPPPPPPPP")
    print()

    battle(hero, goblin)

if __name__ == "__main__":
    main()
