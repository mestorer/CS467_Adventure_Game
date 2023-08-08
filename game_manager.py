import os
import json
import constants
from room import Room
from item import Item
from door import Door
from story_handler import StoryHandler
from player import Player
from nl_parser import NlParser
from command_processor import CommandProcessor
from helper_functions import print_text

class GameManager:
    def __init__(self):
        self.cur_path = os.path.dirname(__file__)
        self.new_data_dirs = constants.NEW_DATA_DIRS
        self.saved_data_dirs = constants.SAVED_DATA_DIRS
        self.parser = NlParser() # instance allows for potential adding
                                 # or removing from language rules
        self.command_processor = CommandProcessor()
        self.story_handler = StoryHandler()
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
        self.player.prev_checkpoint = self.player.checkpoint - 1

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
        print(constants.colors.PURPLE + 
              constants.OPENING_TITLE + 
              constants.colors.ENDCOLOR)

    def show_intro(self):
        print_text(constants.GAME_INTRO,color=constants.colors.PURPLE, 
                   pause=0.05)
        print(constants.colors.PURPLE + 
              constants.LINE_BREAK +
              constants.colors.ENDCOLOR)
    
    def check_terminal_size(self):
        # Check for the right terminal size
        term_size = os.get_terminal_size()
        if term_size.columns < constants.MIN_TERM_SIZE_COLS:
            print(constants.colors.RED)
            print(f"Error: Minimum of {constants.MIN_TERM_SIZE_COLS} columns " +
                  "required for game!")
            print("Please resize your terminal window and try again.")
            print(constants.colors.ENDCOLOR)
            exit(0)
        if term_size.lines < constants.MIN_TERM_SIZE_LINES:
            print(constants.colors.RED)
            print(f"Error: Minimum of {constants.MIN_TERM_SIZE_LINES} lines " +
                  "required for game!")
            print("Please resize your terminal window and try again.")
            print(constants.colors.ENDCOLOR)
            exit(0)
          
    def load_prompt(self):
        # Ask player if they want to start a new game or load a saved game
        while True:
            print(constants.colors.GREEN + 
                  "Would you like to load a saved game or start a " +
                  "new one? (load / new / exit)" + 
                  constants.colors.ENDCOLOR)
            new_or_saved = input("> ")
            new_or_saved = new_or_saved.strip().lower()
            if new_or_saved == 'new':
                print()
                print(constants.colors.GREEN + 
                      "Would you like to see a short introduction to the " + 
                      "game? (y / n):\n" +
                      "**Recommended for first time players**" +
                      constants.colors.ENDCOLOR)
                see_intro = input("> ")
                os.system('clear')  # Clear screen
                if see_intro.lower() == 'y' or see_intro.lower() == 'yes':
                    self.show_intro()
                self.instantiate_objects()
                return False
            elif new_or_saved == 'load':
                self.execute_user_command(['loadgame'])
                return True
            elif new_or_saved == 'exit':
                os.system('clear')  # Clear screen 
                exit(0)
            else:
                print(constants.colors.RED +
                      "I'm sorry, but I didn't understand your response" +
                      constants.colors.ENDCOLOR + "\n") 
                
    def update_score(self):
        """
        Updates player score based on valid commands entered
        """
        self.player.total_score += 1      
    
    def update_game_state(self, player, item_list):
        """
        Display story if player has reached a new checkpoint.
        Update item descriptions if player has picked up a key item
        """
        self.story_handler.check_story(player, item_list)
        new = self.check_end_game()
        return new
        
    def display_final_score(self):
        """
        Display the player's final score and performance report.
        """
        print_text(constants.GAME_OUTRO,color=constants.colors.GREEN, 
                   newline=False)
        print_text("Press enter to continue...")
        enter = input()
        os.system('clear')  # Clear screen
        print_text(constants.LINE_BREAK)
        print_text("PERFORMANCE REPORT:", newline=False)
        if self.player.total_score < 100:
            print_text("OVERALL GRADE: A")
            print_text(constants.SCORE_RESULTS["A"])
        elif self.player.total_score < 120:
            print_text("OVERALL GRADE: B")
            print_text(constants.SCORE_RESULTS["B"])
        elif self.player.total_score < 140:
            print_text("OVERALL GRADE: C")
            print_text(constants.SCORE_RESULTS["C"])
        elif self.player.total_score < 160:
            print_text("OVERALL GRADE: D")
            print_text(constants.SCORE_RESULTS["D"])
        else:
            print_text("OVERALL GRADE: F")
            print_text(constants.SCORE_RESULTS["F"])
        print_text("-- Management")
        print_text(constants.LINE_BREAK)
    
    def check_end_game(self):
        """
        Display game over message and exit game.
        """
        if (self.player.location == "Executive Office" and 
            self.player.checkpoint) == 10:
            self.display_final_score()
            new_game = self.play_again()
            return new_game
        return None
            
    def play_again(self):
        """
        Prompt user to play again or exit game.
        """
        while True:
            print_text("Would you like to play again? (y / n)")
            response = input(">")
            if response == 'y' or response == 'yes':
                return True
            elif response == 'n' or response == 'no':
                return False
            else:
                print_text("I'm sorry, but I didn't understand your response", 
                           color=constants.colors.RED, newline=False)    

    def start_game(self):
        self.check_terminal_size() # Check for minumum size and exit if not.
        os.system('clear') 
        self.show_title()
        load = self.load_prompt()
        
        if (load == False or
            (load == True and self.player.location == "Hidden Start")):
            self.update_game_state(self.player, self.item_list)
            self.execute_user_command(['go', 'parking lot'])
        
        while True:
            state = self.update_game_state(self.player, self.item_list)
            if state is None:    # Game not over
                pass
            elif state:
                return True
            else:
                return False
            user_input = input(">")
            command = self.parse_user_input(user_input)
            if command:
                self.execute_user_command(command)
                self.update_score()
            else:
                print()
                print(constants.colors.RED +
                      "I'm sorry, but I didn't understand your response" +
                      constants.colors.ENDCOLOR + "\n")
