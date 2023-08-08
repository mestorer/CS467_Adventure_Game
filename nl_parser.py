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
        if (len(tokens) == 1): # handles 'look' or 'l' command with no target
            return ['look']
        else:
            if tokens[0] == "look" and tokens[1] == "at":
                new_command = ['look at'] + tokens[2:]
                return self._merge_item_names(new_command)
            elif tokens[0] == "inspect" or tokens[0] == "examine":
                new_command = ['look at'] + tokens[1:]
                return self._merge_item_names(new_command)
            else:
                return None
    
    # combine tokens into item names       
    def _merge_item_names(self, tokens):
        if len(tokens) == 1:
            return None
        
        modified_tokens = [tokens[0]]
        item_name = ""
        
        for i in range(1,len(tokens)):
            if tokens[i] == "on" or tokens[i] == "with":    
                #take off the extra space
                modified_tokens.append(item_name[0:len(item_name)-1])
                modified_tokens.append(tokens[i])
                item_name = ""
                continue
            item_name += tokens[i]
            if i != len(tokens) - 1:
                item_name += " "
        modified_tokens.append(item_name)
        return modified_tokens

    # keeps track of commands that target items
    item_commands = ['take', 'use', 'drop', 'throw', 'taste', 
                     'touch', 'smell', 'shake', 'break', 'read',
                     'grab', 'combine', 'toss', 'lick', 'rub',
                     'feel', 'sniff', 'inhale', 'rock', 'smash',
                     'crush']

    # Check if tokenized input matches established language rules
    def parse_command(self, input_text):
        
        if len(input_text) == 0:
            return None
        
        tokens = self._tokenize(input_text)
        command = tokens[0]
        
        if command in self.language:
            #special cases
            if (command == 'look' or 
               command == 'inspect' or
               command == 'examine' or
               command == 'l'):
                return self._handle_look(tokens)
            
            if command == 'go':
                return self._handle_go(tokens)
            
            if command in self.item_commands: 
                return self._merge_item_names(tokens)
            
            # ddetects correct length command for input with no target
            if len(tokens) == len(self.language[command]) + 1:
                return tokens
        
        # movement without explicit 'go' command
        # just a cardinal direction
        elif len(tokens) == 1 and command in self.locations: 
            return ['go', tokens[0]]
        elif len(tokens) == 2 and (tokens[0] + " " + tokens[1]) \
            in self.locations: #just a location name;unsplit
            modified_tokens = self._unsplit_location_name(tokens)
            return modified_tokens
        
        # not a valid command
        return None
    