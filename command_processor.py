from language_library import LanguageLibrary
from helper_functions import print_text, print_slowly
import os
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
            print_text(item.description)
            print()
        else:
            print_text('There is no ' + item_name + ' here.\n', color=constants.colors.RED)
            print()
    
    def _pick_up_item(self, item_name, player, room_list, item_list):
        """
        Adds passed item to player's inventory attribute and removes it from room it was in.
        Returns dialogue to be printed to the screen.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is None or (item_name not in room.items and item_name not in room.dropped_items):
            print_text(f"There is no {item_name} here.\n", color=constants.colors.RED)
            print()
        elif item.is_takeable and (item_name in room.items or item_name in room.dropped_items):
            if item_name in room.items:
                # item is only added to item_flags when it comes from room.items 
                player.item_flags.append(item_name)
                item.remove_hints(item_list) 
            self._transfer_room_item_to_player(player.location, item_name, player, room_list)
            print_text(f"You picked up the {item_name}.\n")
            print()
        else:
            print_text(f"You can't pick up the {item_name}.\n", color=constants.colors.RED)
            print()

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
            print_text(f"You don't have a {item_name} to drop.\n", color=constants.colors.RED)
            print()
        else:
            self._transfer_player_item_to_room(player.location, item_name, player, room_list)
            print_text(f"You dropped the {item_name} on the floor.\n")
            print()
            
    def _throw_item(self, item_name, player, room_list, item_list):
        """
        Adds passed item to room's dropped items attribute and removes it from player's inventory.
        Same as _drop_item, but with different dialogue.
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is not None and (item_name in room.items or item_name in room.dropped_items):
            print_text("You need to take the " + item_name + " first.\n", color=constants.colors.RED)
            print()
        elif item is None or item_name not in player.inventory:
            print_text(f"You don't have a {item_name} to throw. But you wish you did...\n", color=constants.colors.RED)
            print()
        else:
            if item_name == 'stink bomb': #special case for stink bomb in receptionist area
                self._execute_stink_bomb(item, player, room, item_list) #does not drop stink bomb
            else:
                self._transfer_player_item_to_room(player.location, item_name, player, room_list)
                print_text(item.throw)
                print()

    def _transfer_player_item_to_room(self, room_name, item_name, player, 
                                     room_list):
        """
        Helper function for _drop_item and _throw_item.
        Removes the item from the player's inventory and adds it to the room's.
        """
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
                        move_player, message = door.try_to_open(player)
                        print_text(message)
                        print()
                if move_player:
                    player.location = current_room.locations[key][0]
                    #print(f"You are now in the {player.location}")
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
                print()

    def _check_inventory(self, player):
        """
        Prints the items in the player's inventory if they have any.
        """
        if player.inventory == []:
            print_text("Your pockets are empty.\n")
            print()
        else:
            print_text(f"Your pockets contain: {player.inventory}\n")
            print()
            
    def _use_item(self, item_name, player, room_list, item_list):
        """
        Prints the use message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if item is None or (item_name not in room.items and item_name not in room.dropped_items and item_name not in player.inventory):
            print_text(f"There is no {item_name} to use.\n", color=constants.colors.RED)
            print()
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
            print_text("There is probably a better place to use this.\n", color=constants.colors.RED)
            print()
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
            print_text("One or more items is invalid.\n", color=constants.colors.RED)
            print()
            
        elif (self._check_item_in_same_room(item_1, player, room) and
              self._check_item_in_same_room(item_2, player, room)) == False:
            print_text("Not all items in inventory or room.\n", color=constants.colors.RED)
            print()
            
        elif item_1.name not in item_2.combine or item_2.name not in item_1.combine:
            print_text("You can't combine those items.\n", color=constants.colors.RED)
            print()
            
        else:
            self._remove_prereqs(item_1.name, player, room, item_list)
            self._remove_prereqs(item_2.name, player, room, item_list)
            player.inventory.append(item_1.combine[item_2.name])
            print_text(constants.RESULT_TEXT[item_1.combine[item_2.name]])
            print()
            print_text(f"You now have a {item_1.combine[item_2.name]}!\n")
            print()
            
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
    
    def _check_item_in_same_room(self, item, player, room):
        """
        Checks if item is in the same room as the player
        """
        if (item.name not in player.inventory and
              item.name not in room.items and
              item.name not in room.dropped_items):
            return False
        else:
            return True
            
    def _taste_item(self, item_name, player, room_list, item_list):
        """
        Returns the taste message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to taste here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.taste)
            print()
    
    def _touch_item(self, item_name, player, room_list, item_list):
        """
        Returns the touch message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to touch here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.touch)
            print()
    
    def _smell_item(self, item_name, player, room_list, item_list):
        """
        Returns the smell message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to smell here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.smell)
            print()
    
    def _shake_item(self, item_name, player, room_list, item_list):
        """
        Returns the shake message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to shake here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.shake)
            print()
    
    def _break_item(self, item_name, player, room_list, item_list):
        """
        Returns the break message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to break here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.break_item)
            print()
    
    def _read_item(self, item_name, player, room_list, item_list):
        """
        Returns the read message of the item passed in the argument
        """
        item = self._get_game_object_by_name(item_name, item_list)
        room = self._get_game_object_by_name(player.location, room_list)
        if (item is None or 
            self._check_item_in_same_room(item, player, room) == False):
            print_text("There is no such item to read here.\n", color=constants.colors.RED)
            print()
        else:
            print_text(item.read)
            print()
    
    def _print_help_guide(self):
        """
        Prints a help guide for the player describing the commands available 
        to them.
        """
        print_slowly(constants.HELP_GUIDE, pause=0.0)
        print()

    def execute_command(self, command, player, room_list,
                        item_list, door_list, load_game, save_game):
        """
        Executes the command passed in the argument if it is valid.
        """
        if command[0] == 'look':
            self._describe_location(player, room_list, long_desc=True)
            
        elif command[0] == 'look at':
            self._describe_item(command[1], player, room_list, item_list,)
                
        elif command[0] == 'go':
            destination = command[1]
            self._move_player_to_new_room(destination, player, room_list, 
                                          door_list)
        
        elif command[0] in ['take', 'grab']:
            item_to_take = command[1]
            self._pick_up_item(item_to_take, player, room_list, item_list)
                
        elif command[0] in ['use', 'combine']:
            if len(command) == 2 and command[0] == 'use':
                item_to_use = command[1]
                self._use_item(item_to_use, player, room_list, item_list)
            elif len(command) == 4 and (command[2] == 'on' or 
                                        command[2] == 'with'):
                self._combine_items(command[1], command[3], player, room_list,
                                    item_list)
            else:
                print_text("Items can't be used like that.\n", color=constants.colors.RED)
                
        elif command[0] == 'drop':
            self._drop_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['throw', 'toss']:
            self._throw_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['taste', 'lick']:
            self._taste_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['touch', 'rub', 'feel']:
            self._touch_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['smell', 'sniff', 'inhale']:
            self._smell_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['shake', 'rock']:
            self._shake_item(command[1], player, room_list, item_list)
            
        elif command[0] in ['break', 'smash', 'crush']:
            self._break_item(command[1], player, room_list, item_list)
            
        elif command[0] == 'read':
            self._read_item(command[1], player, room_list, item_list)
                
        elif command[0] in ['help', 'h']:
            self._print_help_guide()
        
        elif command[0] in ['inventory', 'i']:
            self._check_inventory(player)
                
        elif command[0] in ['savegame', 'sg', 'save']:
            save_game()
            print_text("Game saved!\n", color=constants.colors.GREEN)
            print()
            
        elif command[0] in ['loadgame', 'lg', 'load']:
            load_game(load_saved_game=True)
            os.system('clear')  # Clear screen
            print_text("Game loaded!\n", color=constants.colors.GREEN)
            print()
            #this is where recap story function from story handler would go
            
            
        elif command[0] in ['quitgame', 'qg', 'quit']:
            os.system('clear')  # Clear screen 
            exit(0)