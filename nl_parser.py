from language_library import LanguageLibrary

class NlParser(LanguageLibrary):
    def __init__(self):
        super().__init__()

    # break input into tokens
    def _tokenize(self,input_text):
        return input_text.lower().split()
    
    # unsplit location names for easier command execution
    def _unsplit_location_name(self, tokens):
        if len(tokens) == 2:
            return ['go', tokens[0] + " " + tokens[1]]
        if len(tokens) == 3:
            return [tokens[0], tokens[1] + " " + tokens[2]]
    
    # handle 'go' special case
    def _handle_go(self, tokens):
        if (len(tokens) == 2): # handles 'go' + cardinal direction
            if tokens[1] not in self.locations:
                return None
            else:
                return tokens
        elif (len(tokens) == 3): # unsplit location name for 'go' command
            if tokens[1] + " " + tokens[2] in self.locations:
                modified_tokens = self._unsplit_location_name(tokens)
                return modified_tokens
            else:
                return None
    
    # handle 'look' special case
    def _handle_look(self, tokens):
        if (len(tokens) == 1): # handles 'look' command with no target
            return tokens
        elif (len(tokens) == 3): # handles 'look at' command
            if tokens[1] == "at":
                return ['look at', tokens[2]]
            if tokens[1] != "at":
                return None

    # Check if tokenized input matches established language rules
    def parse_command(self, input_text):
        
        if len(input_text) == 0:
            return None
        
        tokens = self._tokenize(input_text)
        command = tokens[0]
        
        if command in self.language:
            #special cases
            if command == 'look':
                return self._handle_look(tokens)
            if command == 'go':
                return self._handle_go(tokens)
            
            # default - detects correct length command
            if len(tokens) == len(self.language[command]) + 1:
                return tokens
        
        # movement without explicit 'go' command
        elif len(tokens) == 1 and command in self.locations: # just a cardinal direction
            return tokens
        elif len(tokens) == 2 and (tokens[0] + " " + tokens[1]) in self.locations: #just a location name;unsplit
            modified_tokens = self._unsplit_location_name(tokens)
            return modified_tokens
        
        # not a valid command
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