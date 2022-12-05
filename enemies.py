"""Enemies stuff."""
from typing import Any
from ui import display_board

MAP = [['.' for _ in range(10)] for _ in range(10)]

MENU_LIST = ['Create new enemy',
             'Place enemy on map',
             'Kill enemy']

ENEMIES: dict[str, dict[str, Any]] = {
    "rat": {"health": 10,
            "damage": 1,
            "symbol": "r",
            "location": (0, 0),
            "loot_table": ["cheese"]},
    "goblin": {"health": 30,
               "damage": 3,
               "symbol": "g",
               "location": (0, 0),
               "loot_table": ["gold coins"]},
    "wolf": {"health": 20,
             "damage": 2,
             "symbol": "w",
             "location": (0, 0),
             "loot_table": ["meat"]},
    "donkey": {"health": 50,
               "damage": 5,
               "symbol": "d",
               "location": (0, 0),
               "loot_table": ["key"]}
}

SPAWNED_ENEMIES: list[str] = []


def create_enemy(enemy_type: str) -> dict[str, Any]:
    """Create new instance of an enemy."""
    spawned = [item for item in SPAWNED_ENEMIES if enemy_type in item]
    name = enemy_type + '0'
    instance = 0
    while name in spawned:
        instance += 1
        name = name[:-1] + str(instance)
    new_enemy = ENEMIES[enemy_type]
    SPAWNED_ENEMIES.append(name)
    return new_enemy


def place_enemy(name: str, coordinates: tuple[int, int]) -> None:
    """Place enemy on selected coordinates."""


def kill_enemy(name: str, health: int) -> None:
    """Check if the enemy is dead and do stuff with it."""


def menu(option: str) -> None:
    """Test menu."""
    if option == '1':
        enemy_type = input("rat, goblin, wolf, donkey\n")
        new_enemy = create_enemy(enemy_type)
        print(new_enemy)
    if option == '2':
        enemy_name = input(f"select enemy\n{SPAWNED_ENEMIES}\n")
        new_location: tuple[int, int] = tuple(int(num)  # type: ignore
                                              for num in input("coords x,y")
                                              .split(","))
        place_enemy(enemy_name, new_location)
        display_board(MAP)
    if option == '3':
        enemy_name = input(f"select enemy\n{SPAWNED_ENEMIES}\n")
        health = int(input("current health\n"))
        kill_enemy(enemy_name, health)
        print(SPAWNED_ENEMIES)


def main():
    """Beep boop."""
    option = ''
    while option != 'q':
        i = 1
        for item in MENU_LIST:
            print(f'{i} {item}')
        option = input()
        menu(option)


if __name__ == '__main__':
    main()
