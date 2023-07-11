from language_library import LanguageLibrary

class CommandProcessor(LanguageLibrary):
    def __init__(self):
        super().__init__()
    
    def _get_game_object_by_name(self, name, obj_list):
        """
        Returns the actual game object with the matching name attribute or
        None if there's no match.
        """
        for obj in obj_list:
            if obj.name == name:
                return obj
            
    def _describe_location(self, player, room_list):
        # This will also get more deteiled as we develop the game. Maybe worth
        # considering adding a counter to the room for number of visits so we
        # can display a different description (short), or making a list a short
        # descriptions with progressively helpful hints.
        location = self._get_game_object_by_name(player.location, room_list)
        print(location.description + '\n' + location.directions)

    def _describe_item(self, item_name, player, room_list, item_list ):
        """
        Returns the description of the item passed in the argument if
        it is in the player's inventory or in the room they are in.
        """
        location = self._get_game_object_by_name(player.location, room_list)
        if item_name in location.items or item_name in location.dropped_items or item_name in player.inventory:
            item = self._get_game_object_by_name(item_name, item_list)
            print(item.description)
        else:
            print('There is no ' + item_name + ' here.')
            
            
    def execute_command(self, command, player, room_list, item_list):
        if command[0] == 'look':
            self._describe_location(player, room_list)
            
        elif command[0] == 'look at':
            self._describe_item(command[1], player, room_list, item_list)
                
        elif command[0] == 'go':
            pass
        elif command[0] == 'take':
            pass
        elif command[0] == 'help':
            pass
        elif command[0] == 'inventory':
            pass
        elif command[0] == 'savegame':
            pass
        elif command[0] == 'loadgame':
            pass