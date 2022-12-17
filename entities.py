"""Create game entity."""


from typing import Any
from random import randint, choices


class Entity:
    """Game entity class."""

    spawned: list[str] = []
    instance: dict[str, dict[str, Any]] = {}
    used_names: list[str] = []

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
        self.location: tuple[int, int] = (0, 0)
        self.loot: list[str] = template[9].split(',')
        self.prevfield: str = ''
        if self.name != 'player':
            self.chance: list[int] = [int(self.loot.pop(3)) for _ in range(3)]
        Entity.instance.update(
            {self.name: {'health': self.maxhealth, 'location': self.location}})

    def __del__(self) -> None:
        """Remove entity."""
        if self.name == 'player':
            print('You are dead. Better luck next time!')
        else:
            print(f'{self.name} was killed')

    def remove_from_enemy_list(self, enemies_list: list[Any]) -> None:
        """Delete entity object from enemies list."""
        del enemies_list[Entity.used_names.index(self.name)]

    def get_name(self, name: str) -> str:
        """Get unique mob name."""
        if name == 'player':
            return name
        new_name: str = name + '0'
        instance: int = 0
        while new_name in Entity.used_names:
            instance += 1
            if len(str(instance)) == 1 or instance == 10:
                new_name = new_name[:-1] + str(instance)
            elif len(str(instance)) == 2:
                new_name = new_name[:-2] + str(instance)
        Entity.used_names.append(new_name)
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

    def recieve_damage(self, enemies_list: list[Any], damage: int) -> None:
        """Recieve damage from attacker."""
        self.health -= damage
        current_health: int = self.health if self.health >= 0 else 0
        print(
            f'{self.name} has {current_health} health left')
        Entity.instance[self.name]['health'] = current_health
        if self.health <= 0:
            Entity.instance.pop(self.name)
            Entity.spawned.pop(Entity.spawned.index(self.name))
            Entity.remove_from_enemy_list(self, enemies_list)

    def deal_damage(self) -> int:
        """Deal damage to defender."""
        damage: int = sum([randint(1, int(self.roll))
                           for die in range(int(self.dice))])
        if self.name == 'player':
            print(f'{self.name} dealt {damage} damage')
        else:
            print(f'{self.name} dealt {damage} damage')
        return damage

    def spawn(self, board: list[list[str]]) -> None:
        """Place entity on board."""
        i: int = randint(0, len(board)-2)
        j: int = randint(0, len(board[0])-2)
        while board[i][j] not in ['0', '1', '2', '3', '4']:
            i = randint(0, len(board)-2)
            j = randint(0, len(board[0])-2)
        Entity.instance[self.name]['location'] = i, j
        Entity.spawned.append(self.name)
        self.location = i, j
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
        row, col = enemy.instance[enemy.name]['location']
        level_board[row][col] = enemy.symbol
