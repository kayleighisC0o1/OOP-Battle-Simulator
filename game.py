from goblin import Goblin


ARENA_NAME = "The Bumble clot"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("BeeWasiner")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But who is waxing their heads bald no one... yet.")


if __name__ == "__main__":
    main()
