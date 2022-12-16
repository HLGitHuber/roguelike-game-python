"""Hardcoded maps and enemies lists."""
from typing import Any
import entities as ent

enemies0: list[Any] = [ent.Entity('rat') for _ in range(
    15)] + [ent.Entity('wolf') for _ in range(10)]
enemies1: list[Any] = [ent.Entity('rat') for _ in range(
    15)] + [ent.Entity('goblin') for _ in range(10)]
enemies2: list[Any] = [ent.Entity('goblin') for _ in range(
    15)] + [ent.Entity('demon') for _ in range(10)]
enemies3: list[Any] = [ent.Entity('demon') for _ in range(
    10)] + [ent.Entity('goblin') for _ in range(10)] + [ent.Entity('bat')
                                                        for _ in range(20)]


def get_board(filename: str) -> list[list[str]]:
    """Get file content."""
    with open(filename, 'r', encoding='UTF-8') as file:
        string_map: list[list[str]] = [list(line)[:-1] for
                                       line in file.readlines()]
        map_proper: list[list[str]] = [list(line) for line in string_map]
        return map_proper


base_map0: list[list[str]] = get_board('maps/map0.txt')
base_map1: list[list[str]] = get_board('maps/map1.txt')
base_map2: list[list[str]] = get_board('maps/map2.txt')
base_map3: list[list[str]] = get_board('maps/map3.txt')
base_map4: list[list[str]] = get_board('maps/map4.txt')

temp_map0: list[list[str]] = get_board('maps/map0.txt')
temp_map1: list[list[str]] = get_board('maps/map1.txt')
temp_map2: list[list[str]] = get_board('maps/map2.txt')
temp_map3: list[list[str]] = get_board('maps/map3.txt')

ent.spawn_enemies(enemies0, temp_map0)
ent.spawn_enemies(enemies1, temp_map1)
ent.spawn_enemies(enemies2, temp_map2)
ent.spawn_enemies(enemies3, temp_map3)
