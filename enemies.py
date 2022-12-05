"""Enemies stuff."""
from typing import Any
from ui import display_board


class Stuff:
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

    ENEMY_STATS: dict[str, dict[str, Any]] = {}


def create_enemy(enemy_type: str) -> None:
    """Create new instance of an enemy."""
    spawned = [item for item in Stuff.ENEMY_STATS if enemy_type in item]
    name = enemy_type + '0'
    instance = 0
    while name in spawned:
        instance += 1
        name = name[:-1] + str(instance)
    new_enemy = Stuff.ENEMIES[enemy_type]
    Stuff.ENEMY_STATS.update({name: new_enemy})


def place_enemy(name: str, coordinates: tuple[int, int]) -> None:
    """Place enemy on selected coordinates."""
    row, col = coordinates
    Stuff.SPAWNED_ENEMIES.append(name)
    Stuff.ENEMY_STATS[name]['location'] = coordinates
    Stuff.MAP[row][col] = Stuff.ENEMY_STATS[name]['symbol']


def kill_enemy(name: str, health: int) -> None:
    """Check if the enemy is dead and do stuff with it."""
    if health <= 0:
        row, col = Stuff.ENEMY_STATS[name]['location']
        Stuff.MAP[row][col] = 'X'
        index = Stuff.SPAWNED_ENEMIES.index(name)
        Stuff.SPAWNED_ENEMIES.pop(index)
        Stuff.ENEMY_STATS.pop(name)
    else:
        print("Stayin' Alive\n Ahh Ahh Ahh Ahh")


def menu(option: str) -> None:
    """Test menu."""
    if option == '1':
        enemy_type = input("rat, goblin, wolf, donkey\n")
        create_enemy(enemy_type)
    if option == '2':
        display_board(Stuff.MAP)
        mobs = list(Stuff.ENEMY_STATS)
        for item in mobs:
            print(item)
        enemy_name = input("select enemy\n")
        new_location: tuple[int, int] = tuple(int(num)  # type: ignore
                                              for num in input("coords x,y")
                                              .split(","))
        place_enemy(enemy_name, new_location)
        display_board(Stuff.MAP)
    if option == '3':
        enemy_name = input(f"select enemy\n{Stuff.SPAWNED_ENEMIES}\n")
        health = int(input("current health\n"))
        kill_enemy(enemy_name, health)
        print(Stuff.SPAWNED_ENEMIES)


def main():
    """Beep boop."""
    option = ''
    while option != 'q':
        i = 1
        for item in Stuff.MENU_LIST:
            print(f'{i} {item}')
            i += 1
        option = input()
        menu(option)


if __name__ == '__main__':
    main()
