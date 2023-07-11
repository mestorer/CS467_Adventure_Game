import os
import json
import constants
from room import Room
from item import Item
from player import Player
from nl_parser import NlParser
from command_processor import CommandProcessor

class GameManager:
    def __init__(self):
        self.cur_path = os.path.dirname(__file__)
        self.new_data_dirs = constants.NEW_DATA_DIRS
        self.saved_data_dirs = constants.SAVED_DATA_DIRS
        self.parser = NlParser() # instance allows for potential adding/ removing from language rules
        self.command_processor = CommandProcessor()
        self.player = None
        self.room_list = []
        self.item_list = []

    def instantiate_objects(self, load_saved_game=False):
        """
        Instantiates all the game objects from data files.
        If load_saved_game is True, it loads objects from files that contain
        a game previously saved.
        """
        if not load_saved_game:
            obj_files = self._get_obj_file_list(self.new_data_dirs)
        else:
            obj_files = self._get_obj_file_list(self.saved_data_dirs)
            if len(obj_files) == 1:
                obj_files = self._get_obj_file_list(self.new_data_dirs)
        self._build_objects(obj_files)

    def _build_objects(self, obj_files):
        """
        Builds all objects from files into the correct object type by sorting
        by data directory name. The data directories are passed in the 
        obj_files argument.
        """
        for obj_file in obj_files:
            file_name = obj_file.split('/')[-1]
            with open(obj_file, "r") as read_file:
                data = json.load(read_file)
            if 'room_data' in obj_file:
                room = Room(file_name, data)
                self.room_list.append(room)
            elif 'item_data' in obj_file:
                item = Item(file_name, data)
                self.item_list.append(item)
            else:
                self.player = Player(file_name, data)

    def save_objects_to_file(self):
        """
        Saves game object state to file to allow the game to be resumed
        by the player
        """
        # Save player
        saved_obj_path = self.cur_path + self.saved_data_dirs[0]
        self._save_object(saved_obj_path, self.player) 
        # Save rooms
        saved_obj_path = self.cur_path + self.saved_data_dirs[1]
        for room in self.room_list:
            self._save_object(saved_obj_path, room)

    def _save_object(self, saved_obj_path, obj):
        """
        Saves individual object to file.
        """
        file_name = (obj.file_name)
        with open(saved_obj_path + file_name, "w") as write_file:
            json.dump(obj, write_file, default=obj.serialize_as_json)

    def _get_obj_file_list(self, data_dirs):
        """
        Returns a list of all the object data files in selected directories.
        """
        obj_files = []
        for dir_name in data_dirs:
            new_obj_path = self.cur_path + dir_name
            # Get all filenames in folder that end in 'json'
            for filename in os.scandir(new_obj_path):
                if filename.is_file() and str(filename.path)[-4:] == 'json':
                    obj_files.append(filename.path)
        return obj_files

    def parse_user_input(self, user_input):
        """
        Returns array of command tokens from user input if valid.
        If invalid, returns None.
        """
        command = self.parser.parse_command(user_input)
        return command
    
    def execute_user_command(self, command):
        """
        Executes the command passed in the argument.
        """
        self.command_processor.execute_command(command)
        
    def pick_up_item(self, item_name):
        """
        Adds passed item to player's inventory attribute and removes it from
        the room it was in.
        """
        item = self._get_game_object_by_name(item_name, self.item_list)
        if item.is_takeable:
            self.transfer_room_item_to_player(self.player.location, item_name)
            return True
        return False

    def transfer_room_item_to_player(self, room_name, item_name):
        room = self._get_game_object_by_name(room_name, self.room_list)
        room.items.remove(item_name)
        self.player.inventory.append(item_name)

    def drop_inventory_item_in_room(self, room_name, item_name):
        room = self._get_game_object_by_name(room_name, self.room_list)
        room.dropped_items.append(item_name)
        self.player.inventory.remove(item_name)

    def _get_game_object_by_name(self, name, obj_list):
        """
        Returns the actual game object with the matching name attribute or
        None if there's no match.
        """
        for obj in obj_list:
            if obj.name == name:
                return obj

    def can_item_be_taken(self, item):
        return item.is_takeable

    def move_player_to_new_roow(self, room_name):
        self.player.location = room_name

    def describe_location(self):
        # This will also get more deteiled as we develop the game. Maybe worth
        # considering adding a counter to the room for number of visits so we
        # can display a different description (short), or making a list a short
        # descriptions with progressively helpful hints.
        location = self._get_game_object_by_name(self.player.location,
                                                 self.room_list)
        print(location.description)

    def start_game(self):
        # Some ASCII art about the game or a basic despcription should go here.
        # Before the game starts...
        # Also need to clear screen, make sure size is adequate, etc
        # Maybe offer a short tutorial when a new game is started
        
        os.system('clear')  # Clear screen
        
        # Ask player if they want to start a new game or load a saved game
        while True:
            new_or_saved = input("Do you want to start a new or a saved " +
                                    "game? (new / loadgame / exit)\n" + ">")
            new_or_saved = new_or_saved.strip().lower()
            if new_or_saved == 'new':
                self.instantiate_objects()
                break
            elif new_or_saved == 'loadgame':
                self.instantiate_objects(load_saved_game=True)
                break
            elif new_or_saved == 'exit':
                exit(0)
            else:
                print("I'm sorry, but I didn't understand your response")
                    
        os.system('clear')  # Clear screen       
        while True:
            user_input = input(">")
            command = self.parse_user_input(user_input)
            if command:
                print(command) # debug/demo
                self.execute_user_command(command)
            else:
                print("I'm sorry, but I didn't understand your response")
        
        self.describe_location()  # Describe location of starting room.
        # The game continues from here once we have at least a couple detailed
        # rooms with descriptions, etc.
