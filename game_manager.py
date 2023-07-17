import os
import json
import constants
from room import Room
from item import Item
from door import Door
from player import Player
from nl_parser import NlParser
from command_processor import CommandProcessor
from helper_functions import print_slowly, print_text

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
        self.door_list = []

    def instantiate_objects(self, load_saved_game=False):
        """
        Instantiates all the game objects from data files.
        If load_saved_game is True, it loads objects from files that contain
        a game previously saved.
        """
        if not load_saved_game:
            obj_files = self._get_obj_file_list(self.new_data_dirs)
        else:
            self.player = None
            self.room_list = []
            self.item_list = []
            self.door_list = []
            obj_files = self._get_obj_file_list(self.saved_data_dirs)
            if len(obj_files) == 0:
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
            elif 'door_data' in obj_file:
                door = Door(file_name, data)
                self.door_list.append(door)
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
        # Save items
        saved_obj_path = self.cur_path + self.saved_data_dirs[2]
        for item in self.item_list:
            self._save_object(saved_obj_path, item)
        # Save transitions
        saved_obj_path = self.cur_path + self.saved_data_dirs[3]
        for trans in self.door_list:
            self._save_object(saved_obj_path, trans)

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
        self.command_processor.execute_command(command, self.player, 
                self.room_list, self.item_list, self.door_list,
                self.instantiate_objects, self.save_objects_to_file)
        
    def show_title(self):
        print(constants.OPENING_TITLE)

    def show_intro(self):
        print_slowly(constants.GAME_INTRO, pause=0.05)

    def start_game(self):
        # Some ASCII art about the game or a basic despcription should go here.
        # Before the game starts...
        # Also need to clear screen, make sure size is adequate, etc
        # Maybe offer a short tutorial when a new game is started
        
        os.system('clear')  # Clear screen

        # Check for the right terminal size
        term_size = os.get_terminal_size()
        if term_size.columns < constants.MIN_TERM_SIZE_COLS:
            print(f"Error: Please resize your terminal to the at least {constants.MIN_TERM_SIZE_COLS} columns required for game!")
            exit(0)
        if term_size.lines < constants.MIN_TERM_SIZE_LINES:
            print(f"Error: Please resize your terminal to the at least {constants.MIN_TERM_SIZE_COLS} lines required for game!")
            exit(0)

        # Show game title
        self.show_title()
        
        # Ask player if they want to start a new game or load a saved game
        while True:
            new_or_saved = input("Do you want to start a new or a saved " +
                                    "game? (new / loadgame / exit)\n" + ">")
            new_or_saved = new_or_saved.strip().lower()
            if new_or_saved == 'new':
                see_intro = input("Would you line to see a short intro to the game if you're playing it for the first time? (y/n): \n" + ">")
                if see_intro.lower() == 'y':
                    self.show_intro()
                self.instantiate_objects()
                break
            elif new_or_saved == 'loadgame':
                self.execute_user_command(['loadgame'])
                break
            elif new_or_saved == 'exit':
                exit(0)
            else:
                print("I'm sorry, but I didn't understand your response")
                    
        #os.system('clear')  # Clear screen       
        while True:
            user_input = input(">")
            command = self.parse_user_input(user_input)
            if command:
                print(command) # debug/demo
                self.execute_user_command(command)
            else:
                print("I'm sorry, but I didn't understand your response")

