class NlParser:
    def __init__(self):
        # defined language rules 
        self.language = {
            'look': ['at', 'target'], # can be used with or without target
            'go': ['location', 'location'], # exact location names always have two words
            'take': ['item'],
            'help': [],
            'inventory': [],
            'savegame': [],
            'loadgame': [],
            'use': ['item', 'on', 'target'], # need at least 9 more verbs
        }

        # all valid locations in the game
        self.locations = ['north', 'south', 'east', 'west', 
                    'n', 's', 'e', 'w',
                    'parking lot', 'reception area', 'supply closet', 'main hallway',
                    'it room', 'server room', 'executive elevator', 'executive office',
                    'marketing department', 'conference room', 'research lab', 'financial department',
                    'archives room']

    # break input into tokens
    def _tokenize(self,input_text):
        return input_text.lower().split()
    
    # unsplit location names for easier command execution
    def _unsplit_location_name(self, tokens):
        if len(tokens) == 2:
            return [tokens[0] + " " + tokens[1]]
        if len(tokens) == 3:
            return [tokens[0], tokens[1] + " " + tokens[2]]

    # Check if tokenized input matches established language rules
    def parse_command(self, input_text):
        tokens = self._tokenize(input_text)
        command = tokens[0]
        
        if command in self.language:
            #special cases
            if ((command == 'look') and (len(tokens) == 1)): # handles 'look' command with no target
                return tokens
            if ((command == 'go') and (len(tokens) == 2)): # handles 'go' + cardinal direction
                return tokens
            if ((command == 'go') and (len(tokens) == 3)): # unsplit location name for 'go' command
                modified_tokens = self._unsplit_location_name(tokens)
                return modified_tokens
            
            #default
            if len(tokens) == len(self.language[command]) + 1:
                return tokens
        
        # movement without explicit 'go' command
        elif len(tokens) == 1 and command in self.locations: # just a cardinal direction
            return tokens
        elif len(tokens) == 2 and (tokens[0] + " " + tokens[1]) in self.locations: #just a location name;unsplit
            modified_tokens = self._unsplit_location_name(tokens)
            return modified_tokens
        
        # not a valid command
        else:
            return None

    '''# validate command usage and execute respective action
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
            print('I do not understand')'''


'''if __name__ == '__main__':
    
    class Player:
        def __init__(self, name, location):
            self.name = name
            self.location = location # location could be an object so that it can be easily modified
            self.inventory = []
    
    player_1 = Player('John', 'room1')    
    while True:
        user_input(player_1)'''