"""Hardcoded maps and enemies lists."""
from typing import Any
import entities as ent


def get_board(filename: str) -> list[list[str]]:
    """Get file content."""
    with open(filename, 'r', encoding='UTF-8') as file:
        string_map: list[list[str]] = [list(list(line)) for
                                       line in file.readlines()]
        return string_map


def find_enemy(coords: list[int], map_index: int) -> int:
    """Find enemy index on monster list."""
    enemy_index: int = 0
    i: int = 0
    for enemy in enemies[map_index]:
        if enemy.location == coords:
            enemy_index = i
        i += 1
    return enemy_index


enemies0: list[Any] = [ent.Entity('rat') for _ in range(
    15)] + [ent.Entity('wolf') for _ in range(10)]
enemies1: list[Any] = [ent.Entity('rat') for _ in range(
    15)] + [ent.Entity('goblin') for _ in range(10)]
enemies2: list[Any] = [ent.Entity('goblin') for _ in range(
    15)] + [ent.Entity('demon') for _ in range(10)]
enemies3: list[Any] = [ent.Entity('demon') for _ in range(
    10)] + [ent.Entity('goblin') for _ in range(10)] + [ent.Entity('bat')
                                                        for _ in range(20)]
enemies: list[list[Any]] = [enemies0, enemies1, enemies2, enemies3]

base_map0: list[list[str]] = get_board('maps/map0.txt')
base_map1: list[list[str]] = get_board('maps/map1.txt')
base_map2: list[list[str]] = get_board('maps/map2.txt')
base_map3: list[list[str]] = get_board('maps/map3.txt')
base_map4: list[list[str]] = get_board('maps/map4.txt')
base_maps: list[list[list[str]]] = [base_map0,
                                    base_map1, base_map2, base_map3, base_map4]

temp_map0: list[list[str]] = get_board('maps/map0.txt')
temp_map1: list[list[str]] = get_board('maps/map1.txt')
temp_map2: list[list[str]] = get_board('maps/map2.txt')
temp_map3: list[list[str]] = get_board('maps/map3.txt')
temp_map4: list[list[str]] = get_board('maps/map4.txt')
temp_maps: list[list[list[str]]] = [temp_map0,
                                    temp_map1, temp_map2, temp_map3, temp_map4]

ent.spawn_enemies(enemies0, temp_map0)
ent.spawn_enemies(enemies1, temp_map1)
ent.spawn_enemies(enemies2, temp_map2)
ent.spawn_enemies(enemies3, temp_map3)
