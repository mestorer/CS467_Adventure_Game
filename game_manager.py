import os
import json
from room import Room
from item import Item
from player import Player

class GamaManager:
    def __init__(self):
        self.cur_path = os.path.dirname(__file__)
        self.player = None
        self.room_list = []
        self.item_list = []
        self.new_data_dirs = [
            '/new_player_data/',
            '/new_room_data/',
            '/item_data/']
        self.saved_data_dirs = [
            '/saved_player_data/',
            '/saved_room_data/']

    def instantiate_objects(self):
        obj_files = []
        for dir_name in self.new_data_dirs:
            new_obj_path = self.cur_path + dir_name
            # Get all filenames in folder that end in 'json'
            for filename in os.scandir(new_obj_path):
                if filename.is_file() and str(filename.path)[-4:] == 'json':
                    obj_files.append(filename.path)  
                    #print(obj_files)
        # Read all files and build game objects from json files
        for obj_file in obj_files:
            with open(obj_file, "r") as read_file:
                data = json.load(read_file)
            if 'room_data' in obj_file:
                room = Room(data)
                self.room_list.append(room)
            elif 'item_data' in obj_file:
                item = Item(data)
                self.item_list.append(item)
            else:
                self.player = Player(data)

    def save_objects_to_file(self):
        obj_files = []
        for dir_name in self.new_data_dirs:
            new_obj_path = self.cur_path + dir_name
            # Get all filenames in folder that end in 'json'
            for filename in os.scandir(new_obj_path):
                if filename.is_file() and str(filename.path)[-4:] == 'json':
                    obj_files.append(filename.path)  
                    #print(obj_files)
        # Read all files and build game objects from json files
        for obj_file in obj_files:
            with open(obj_file, "r") as read_file:
                data = json.load(read_file)
            if 'room_data' in obj_file:
                room = Room(data)
                self.room_list.append(room)
            elif 'item_data' in obj_file:
                item = Item(data)
                self.item_list.append(item)
            else:
                self.player = Player(data)

if __name__ == '__main__':
    game = GamaManager()
    game.instantiate_objects()
    print(game.room_list)
    for item in game.room_list:
        item.to_string()
    for item in game.item_list:
        item.to_string()
    game.player.to_string()