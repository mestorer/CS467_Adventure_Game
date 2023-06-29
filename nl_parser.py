# defined language rules
language = {
    'look': ['at', 'target'], # can be used with or without target
    'go': ['location'],
    'take': ['item'],
    'help': [],
    'inventory': [],
    'savegame': [],
    'loadgame': [],
    'use': ['item', 'on', 'target'], # need at least 9 more verbs
}

locations = ['north', 'south', 'east', 'west', 
             'up', 'down', 'left', 'right',
             'room1', 'room2', 'room3', 'room4',
             'room5', 'room6', 'room7', 'room8',
             'room9', 'room10']

def tokenize(input_text):
    return input_text.lower().split()

def parse_command(tokens):
    command = tokens[0]
    if command in language:
        if ((command == 'look') and (len(tokens) == 1)):
            return tokens
        if len(tokens) == len(language[command]) + 1:
            return tokens
    return None

def execute_command(command, player):
    if command[0] == 'go':
        direction = command[1]
        print(f'You go {direction}')
        #add logic
        
    elif command[0] == 'use':
        item = command[1]
        target = command[3]
        print(f'You use the {item} on the {target}')
        # add logic
    
    elif command[0] == 'take':
        item = command[1]
        player.inventory.append(item)
        print(f'You take the {item}')
        print(f'You now have {player.inventory}')
        # add logic
        
    # need to add logic for other commands
    
def user_input(player):
    """ Gets user input and executes command if available. Modifies player object as needed."""
    input_text = input("Enter a command: ")
    tokens = tokenize(input_text)
    command = parse_command(tokens)
    if command:
        execute_command(command, player)
    else:
        print('I do not understand')


if __name__ == '__main__':
    
    class Player:
        def __init__(self, name, location):
            self.name = name
            self.location = location # location could be an object so that it can be easily modified
            self.inventory = []
    
    player_1 = Player('John', 'room1')    
    while True:
        user_input(player_1)