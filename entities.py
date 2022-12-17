"""Create game entity."""


from typing import Any
from random import randint, choices

spawned: list[str] = []
instance: dict[str, dict[str, Any]] = {}
used_names: list[str] = []


class Entity:
    """Game entity class."""

    def __init__(self, name: str) -> None:
        """Create new entity."""
        template: list[str] = self.get_entity_type(name)
        self.name: str = self.get_name(name)
        self.symbol: str = template[1]
        self.exp: int = int(template[2])
        self.health: int = int(template[3])
        self.maxhealth: int = int(template[4])
        self.str: int = int(template[5])
        self.dice: int = int(template[6])
        self.roll: int = int(template[7])
        self.location: list[int] = [0, 0]
        self.loot: list[str] = template[9].split(',')
        self.prevfield: str = ''
        if self.name != 'player':
            self.chance: list[int] = [int(self.loot.pop(3)) for _ in range(3)]
        instance.update(
            {self.name: {'health': self.maxhealth, 'location': self.location}})

    def remove_from_enemy_list(self, enemies_list: list[Any]) -> None:
        """Delete entity object from enemies list."""
        del enemies_list[used_names.index(self.name)]

    def get_name(self, name: str) -> str:
        """Get unique mob name."""
        if name == 'player':
            return name
        new_name: str = name + '0'
        number: int = 0
        while new_name in used_names:
            number += 1
            if len(str(number)) == 1 or number == 10:
                new_name = new_name[:-1] + str(number)
            elif len(str(number)) == 2:
                new_name = new_name[:-2] + str(number)
        used_names.append(new_name)
        return new_name

    def get_entity_type(self, name: str) -> list[str]:
        """Find entity template."""
        try:
            entity_template: list[str] = []
            with open('enemy_template.txt', "r", encoding='UTF-8') as file:
                file.readline()
                lines: list[str] = file.readlines()
                for line in lines:
                    if line.find(name) != -1:
                        entity_template = line.replace("\n", "").split(';')
            if len(entity_template) == 0:
                raise KeyError
            return entity_template
        except KeyError:
            print("Entity type not found")
            return []
        except IOError:
            print("File not found")
            return []

    def recieve_damage(self, enemies_list: list[Any], dmg_info: tuple[str, int]) -> str:
        """Recieve damage from attacker."""
        text: str = ""
        who = dmg_info[0]
        damage = dmg_info[1]
        self.health -= damage
        current_health: int = self.health if self.health >= 0 else 0
        instance[self.name]['health'] = current_health
        text = f'{who} dealt {damage} damage.'
        if self.health <= 0:
            instance.pop(self.name)
            spawned.pop(spawned.index(self.name))
            Entity.remove_from_enemy_list(self, enemies_list)
            if self.name == 'player':
                text = text + ' You are dead. Better luck next time!'
            else:
                text = text + f' {self.name} was killed'
        return text + '\n'

    def deal_damage(self) -> tuple[str, int]:
        """Deal damage to defender."""
        damage: int = sum([randint(1, int(self.roll))
                           for die in range(int(self.dice))])
        return self.name, damage

    def spawn(self, board: list[list[str]]) -> None:
        """Place entity on board."""
        i: int = randint(0, len(board)-2)
        j: int = randint(0, len(board[0])-2)
        while board[i][j] not in ['0', '1', '2', '3', '4']:
            i = randint(0, len(board)-2)
            j = randint(0, len(board[0])-2)
        instance[self.name]['location'] = [i, j]
        spawned.append(self.name)
        self.location = [i, j]
        self.prevfield = board[i][j]
        board[i][j] = self.symbol

    def drop_item(self) -> str:
        """Roll item drop from drop table."""
        item: str = choices(self.loot, cum_weights=self.chance)[0]
        return item


def spawn_enemies(enemy_list: list[Entity], level_board: list[list[str]]
                  ) -> None:
    """Place all enemies on map."""
    for enemy in enemy_list:
        enemy.spawn(level_board)
