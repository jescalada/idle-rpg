import random
import time
from os import path


def initialize_game() -> dict:
    return {
        'player': load_player(),
        'map': load_map(),
        'enemies': load_enemies()
    }


def new_player(name: str) -> dict:
    return {
        'name': name,
        'hp': 100,
        'max_hp': 100,
        'mp': 100,
        'max_mp': 100,
        'equipment': {
            'head': None,
            'neck': None,
            'chest': None,
            'left_hand': None,
            'right_hand': None,
            'left_finger': None,
            'right_finger': None,
            'arms': None,
            'waist': None,
            'legs': None
        },
        'inventory': [],
        'STR': 10,
        'CON': 10,
        'DEX': 10,
        'PER': 10,
        'INT': 10,
        'WIL': 10,
        'CHA': 10,
        'is_fighting': False,
        'is_alive': True
    }


def load_player() -> dict:
    if not path.exists('player.sav'):
        print("No save file found.")
        name = input("Enter a name: ")
        return new_player(name)
    with open('player.sav') as player_data:
        # todo save to file function and load data function
        pass


def load_map() -> dict:
    return {(x, y): {
        'entity': None,
        'type': 'Grass Tile',
        'icon': '.'
    } for x in range(100) for y in range(100)}


def game_tick(game_status: dict) -> dict:
    if game_status['player']['is_fighting']:
        return battle_tick(game_status)
    # todo move to a random direction [implement intelligent movement AI?]
    roll = random.randint(0, 1000)
    if roll < 100:
        return enemy_encounter(game_status)
    elif roll < 250:
        return random_event(game_status)
    elif roll < 350:
        return item_pickup(game_status)
    return game_status


def enemy_encounter(game_status: dict) -> dict:
    game_status['player']['is_fighting'] = True
    print("Enemy encounter!")
    return game_status


def random_event(game_status: dict):
    print("RANDOM EVENT")
    return game_status


def item_pickup(game_status: dict):
    print("picked up some garbage")
    return game_status


def battle_tick(game_status):
    print('FIGHTING')
    return game_status


def load_enemies() -> list:
    return [{
        'name': f'enemy {i}',
        'hp': 100,
        'max_hp': 100,
        'mp': 100,
        'max_mp': 100,
        'STR': 10,
        'CON': 10,
        'DEX': 10,
        'PER': 10,
        'INT': 10,
        'WIL': 10,
        'CHA': 10
    } for i in range(3)]


def print_game_status(game_status: dict):
    for attribute, value in game_status['player'].items():
        print(f'{attribute}: {value}')


def main():
    game = initialize_game()
    while True:
        game = game_tick(game)
        #print_game_status(game)
        time.sleep(1)


if __name__ == '__main__':
    main()
