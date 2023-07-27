import random

# Define ASCII notations for each element
elements = {
    'player': '  O  ',
    'enemy': '  X  ',
    'key': '  K  ',
    'door': '  D  ',
    'sword': '  S  ',
    'empty': '     ',
    'wall': '  |  ',
}

# Define the rooms
rooms = [
    {
        'description': "You are in Room 1. There's a sword lying on the ground. Be careful!",
        'layout': [
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'sword', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
        ],
        'door': False,
    },
    {
        'description': "You are in Room 2. There are some enemies lurking around. Find the next door.",
        'layout': [
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
            ['wall', 'empty', 'enemy', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'enemy', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
        ],
        'door': True,
    },
    {
        'description': "You are in Room 3. You see a door in front of you. Can you find the key?",
        'layout': [
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'key', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'wall'],
            ['wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall', 'wall'],
        ],
        'door': True,
    },
]

# Player status
player_inventory = []
current_room_index = 0
player_health = 100
player_pos = (1, 1)

def print_room():
    room = rooms[current_room_index]
    print(room['description'])

def print_map():
    room = rooms[current_room_index]
    for i, row in enumerate(room['layout']):
        for j, element in enumerate(row):
            if (i, j) == player_pos:
                print(elements['player'], end="")
            else:
                print(elements.get(element, '     '), end="")  # Use get() to handle the 'empty' element
        print()

def take_action(action):
    global current_room_index, player_pos
    room = rooms[current_room_index]
    old_pos = player_pos

    if action == 'left':
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif action == 'right':
        new_pos = (player_pos[0], player_pos[1] + 1)
    elif action == 'up':
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif action == 'down':
        new_pos = (player_pos[0] + 1, player_pos[1])
    else:
        print("Invalid action. Try again.")
        return False

    if 0 <= new_pos[0] < len(room['layout']) and 0 <= new_pos[1] < len(room['layout'][0]) and room['layout'][new_pos[0]][new_pos[1]] != 'wall':
        player_pos = new_pos
        if room['layout'][new_pos[0]][new_pos[1]] == 'key':
            player_inventory.append('key')
            print("You picked up a Key.")
            room['layout'][new_pos[0]][new_pos[1]] = 'empty'
            print("Find the next door.")
        elif room['layout'][new_pos[0]][new_pos[1]] == 'sword':
            player_inventory.append('sword')
            print("You picked up a Sword.")
            room['layout'][new_pos[0]][new_pos[1]] = 'empty'
            print("Find the next door.")
        elif room['layout'][new_pos[0]][new_pos[1]] == 'enemy' and 'sword' in player_inventory:
            print("You attacked and defeated the enemy!")
            room['layout'][new_pos[0]][new_pos[1]] = 'empty'
        elif room['layout'][new_pos[0]][new_pos[1]] == 'door' and 'key' in player_inventory:
            print("Congratulations! You escaped the dungeon!")
            current_room_index += 1
            if current_room_index >= len(rooms):
                print("You've completed all levels. Congratulations!")
                return True
            player_pos = (1, 1)  # Reset player position for the next room
            return False
        elif room['layout'][new_pos[0]][new_pos[1]] == 'door':
            print("You need a key to open the door.")
        return False
    else:
        print("You cannot move in that direction.")
        return False

def main():
    print("Welcome to the Dungeon Escape!")
    print("Use 'left', 'right', 'up', 'down' to move, 'attack' to fight enemies (if you have a sword), and 'take' to pick up items.")
    print("ASCII notations:")
    for element, notation in elements.items():
        print(f"{notation} = {element.capitalize()}")
    
    while True:
        print_map()
        print_room()

        action = input("Enter your action: ").lower()

        if action in ['left', 'right', 'up', 'down', 'attack', 'take']:
            if take_action(action):
                break
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
