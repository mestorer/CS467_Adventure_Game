from language_library import LanguageLibrary
from helper_functions import print_text
import constants

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
            
    def _describe_location(self, player, room_list, long_desc):
        """
        Returns the long description of the room the player is in.
        Informs player of directions and dropped items available to them.
        """
        location = self._get_game_object_by_name(player.location, room_list)
        messages = location.describe(long_desc=long_desc)
        for message in messages:
            print_text(message)
        print()

    def _describe_item(self, item_name, player, room_list, item_list ):
        """
        Returns the description of the item passed in the argument if
        it is in the player's inventory or in the room they are in.
        """
        location = self._get_game_object_by_name(player.location, room_list)
        if item_name in location.items or item_name in location.dropped_items \
                or item_name in player.inventory:
            item = self._get_game_object_by_name(item_name, item_list)
            print(item.description + '\n')
        else:
            print('There is no ' + item_name + ' here.\n')
    
    def _pick_up_item(self, item_name, player, room_list, item_list):
        """
        Adds passed item to player's inventory attribute and removes it from room it was in.
        Returns dialogue to be printed to the screen.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is None or (item_name not in room.items and item_name not in room.dropped_items):
            print(f"There is no {item_name} here.\n")
        elif item.is_takeable and (item_name in room.items or item_name in room.dropped_items):
            self._transfer_room_item_to_player(player.location, item_name, player, room_list)
            print(f"You picked up the {item_name}.\n")
        else:
            print(f"You can't pick up the {item_name}.\n")

    def _transfer_room_item_to_player(self, room_name, item_name, 
                                      player, room_list):
        """
        Removes the item from the room it is in and adds it to the player's 
        inventory.
        """
        room = self._get_game_object_by_name(room_name, room_list)
        if item_name in room.items:
            room.items.remove(item_name)
        elif item_name in room.dropped_items:
            room.dropped_items.remove(item_name)
        player.inventory.append(item_name)
        
    def _drop_item(self, item_name, player, room_list, item_list):
        """
        Adds passed item to room's dropped items attribute and removes it from player's inventory.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        
        if item is None or item_name not in player.inventory:
            print(f"You don't have a {item_name} to drop.\n")
        else:
            self._transfer_player_item_to_room(player.location, item_name, player, room_list)
            print(f"You dropped the {item_name} on the floor.\n")
            
    def _throw_item(self, item_name, player, room_list, item_list):
        """
        Adds passed item to room's dropped items attribute and removes it from player's inventory.
        Same as _drop_item, but with different dialogue.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is not None and (item_name in room.items or item_name in room.dropped_items):
            print("You need to take the " + item_name + " first.\n")
        elif item is None or item_name not in player.inventory:
            print(f"You don't have a {item_name} to throw. But you wish you did...\n")
        else:
            if item_name == 'stink bomb': #special case for stink bomb in receptionist area
                self._execute_stink_bomb(item, player, room, item_list) #does not drop stink bomb
            else:
                self._transfer_player_item_to_room(player.location, item_name, player, room_list)
                print_text(item.throw)
                print()

    def _transfer_player_item_to_room(self, room_name, item_name, player, 
                                     room_list):
        room = self._get_game_object_by_name(room_name, room_list)
        room.dropped_items.append(item_name)
        player.inventory.remove(item_name)
        
    def _convert_cardinal_direction(self, direction):
        """
        Converts a cardinal direction to a direction name matching Room 
        locations keys.
        """
        if direction == 'n' or direction == 'north':
            return 'N'
        elif direction == 'e' or direction == 'east':
            return 'E'
        elif direction == 's' or direction == 'south':
            return 'S'
        elif direction == 'w' or direction == 'west':
            return 'W'
        else:
            return direction
    
    
    # TODO: refactor this method to add lock checks and check boundaries
    def _move_player_to_new_room(self, destination, player, room_list, 
                                 doors_list):
        """
        Changes the player's location attribute to the destination passed 
        if it is a valid location.
        """
        current_room = self._get_game_object_by_name(player.location, room_list)
        destination = self._convert_cardinal_direction(destination)
        
        # check if destination in keys or values of current_room.directions
        move_player = True
        for key, value in current_room.locations.items():
            if value is not None and destination == key \
                    or destination in [x.lower() for x in value]:
                # Check to see if there is a transition
                for key2, value2 in current_room.doors.items():
                    if value2 is not None and key2 == key:
                        door = self._get_game_object_by_name(value2, doors_list)
                        move_player, message = door.try_open_door(player)
                        print_text(message)
                        print()
                if move_player:
                    player.location = current_room.locations[key][0]
                    print(f"You are now in the {player.location}")
                    room = self._get_game_object_by_name(player.location, 
                                                         room_list)
                    messages = room.describe()
                    room.mark_as_visited()
                    for message in messages:
                        print_text(message)
                    print()
                    break
        else:
            if move_player:
                print_text("You can't go that way.\n", color=constants.colors.RED)

    def _check_inventory(self, player):
        """
        Prints the items in the player's inventory if they have any.
        """
        if player.inventory == []:
            print("Your pockets are empty.\n")
        else:
            print(f"Your pockets contain: {player.inventory}\n")
            
    def _use_item(self, item_name, player, room_list, item_list):
        """
        Prints the use message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is None or (item_name not in room.items and item_name not in room.dropped_items and item_name not in player.inventory):
            print(f"There is no {item_name} to use.\n")
        elif item_name == 'stink bomb':
            self._execute_stink_bomb(item, player, room, item_list)
        else:
            print_text(item.use)
            print()
    
    # this is a unique interaction. It is the only one in the game that I know of.
    # can be handled elsewhere if more interactions like this are added
    def _execute_stink_bomb(self, item, player, room, items_list):
        """
        Changes the state of Reception Area if stink bomb is used
        """
        if room.name != 'Reception Area':
            print("There is probably a better place to use this.\n")
        else:
            print_text(item.use)
            print()
            self._remove_prereqs('stink bomb', player, room, items_list)
            room.description = "The reception area is a mess. The receptionist is nowhere to be seen."
            room.short_description = "The reception area is a mess."
            keycard_terminal = self._get_game_object_by_name('keycard terminal', items_list)
            keycard_terminal.use = "I should be able to use this now. If only I had a blank keycard."
            keycard_terminal.combine["blank keycard"] = "access card"
                
    def _combine_items(self, item1_name, item2_name, player, room_list, item_list):
        """
        Combines two items if they can be combined. Remove prereqs if in inventory
        """
        item_1 = self._get_game_object_by_name(item1_name, item_list)
        item_2 = self._get_game_object_by_name(item2_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item_1 is None or item_2 is None:
            print("You can't combine those items.\n")
            
        elif (item_1.name not in player.inventory and
              item_1.name not in room.items and
              item_1.name not in room.dropped_items and
              item_2.name not in player.inventory and
              item_2.name not in room.items and
              item_2.name not in room.dropped_items):
            print("Not all items in inventory or room.\n")
            
        elif item_1.name not in item_2.combine or item_2.name not in item_1.combine:
            print("You can't combine those items.\n")
            
        else:
            self._remove_prereqs(item_1.name, player, room, item_list)
            self._remove_prereqs(item_2.name, player, room, item_list)
            player.inventory.append(item_1.combine[item_2.name])
            print_text(constants.RESULT_TEXT[item_1.combine[item_2.name]])
            print()
            print(f"You now have a {item_1.combine[item_2.name]}!\n")
            
    def _remove_prereqs(self, item_name,  player, room, item_list):  
        """
        Removes the prereq item from the appropriate location if takeable.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        if item.name in player.inventory:
            player.inventory.remove(item.name)
        elif item.name in room.items:
            if item.is_takeable:
                room.items.remove(item.name)
        elif item.name in room.dropped_items:
            room.dropped_items.remove(item.name)
            
    
    def _print_help_guide(self):
        """
        Prints a help guide for the player describing the commands available 
        to them.
        """
        print(constants.HELP_GUIDE)

            
    def execute_command(self, command, player, room_list,
                        item_list, door_list, load_game, save_game):
        if command[0] == 'look':
            self._describe_location(player, room_list, long_desc=True)
            
        elif command[0] == 'look at':
            self._describe_item(command[1], player, room_list, item_list,)
                
        elif command[0] == 'go':
            destination = command[1]
            self._move_player_to_new_room(destination, player, room_list, 
                                          door_list)
        
        elif command[0] == 'take':
            item_to_take = command[1]
            self._pick_up_item(item_to_take, player, room_list, item_list)
                
        elif command[0] == 'use':
            if len(command) == 2:
                item_to_use = command[1]
                self._use_item(item_to_use, player, room_list, item_list)
            elif len(command) == 4 and command[2] == 'on':
                self._combine_items(command[1], command[3], player, room_list, item_list)
            else:
                print("Items can't be used like that.\n")
                
        elif command[0] == 'drop':
            self._drop_item(command[1], player, room_list, item_list)
            
        elif command[0] == 'throw':
            self._throw_item(command[1], player, room_list, item_list)
                
        elif command[0] == 'help':
            self._print_help_guide()
        
        elif command[0] == 'inventory':
            self._check_inventory(player)
                
        elif command[0] == 'savegame':
            save_game()
            print("Game saved!\n")
            
        elif command[0] == 'loadgame':
            load_game(load_saved_game=True)
            print("Game loaded!\n")
            
        elif command[0] == 'quitgame':
            exit(0)