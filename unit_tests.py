import unittest
import os
import constants
from game_manager import GameManager
from player import Player
from item import Item
from room import Room

if __name__ == '__main__':
    class TestPlayerClass(unittest.TestCase):
        def setUp(self):
            self.player_file_name = 'player.json'
            self.player_json = {"name": "player", 
                           "inventory": ["inventory"], 
                           "location": ["Reception Area"]}
            self.player_object = Player(self.player_file_name, self.player_json)
            
        def test_constructor(self):
            self.assertEqual(self.player_file_name, 
                             self.player_object.file_name)
            self.assertEqual(self.player_json['name'], 
                             self.player_object.name)
            self.assertEqual(self.player_json['inventory'], 
                             self.player_object.inventory)
            self.assertEqual(self.player_json['location'], 
                             self.player_object.location)
            
        def test_serialize_function(self):
            player_object = Player(self.player_file_name, self.player_json)
            self.assertEqual(self.player_json, 
                             self.player_object.serialize_as_json(player_object))


    class TestItemClass(unittest.TestCase):
        def setUp(self):
            self.item_file_name = 'player.json'
            self.item_json = {"name": "key",
                              "description": "a key that opens somtehing",
                              "is_takeable": True}
            self.item_object = Item(self.item_file_name, self.item_json)

        def test_constructor(self):
            self.assertEqual(self.item_file_name, 
                             self.item_object.file_name)
            self.assertEqual(self.item_json['name'], 
                             self.item_object.name)
            self.assertEqual(self.item_json['description'], 
                             self.item_object.description)
            self.assertEqual(True, 
                             self.item_object.is_takeable)
            
        def test_serialize_function(self):
            item_object = Item(self.item_file_name, self.item_json)
            self.assertEqual(self.item_json, 
                             self.item_object
                             .serialize_as_json(self.item_object))


    class TestRoomClass(unittest.TestCase):
        def setUp(self):
            self.room_file_name = 'room1.json'
            self.room_json = {"name": "Reception Area",
                         "description": "Where you check in as a visitor",
                         "short_description": "Check in",
                         "items": [],
                         "dropped_items": [],
                         "directions": "The Reception Area is connected to \
                            the Main Hallway to the north, the Financial \
                                Department to the east, the Parking Lot to the \
                                    south and a Supply Closet to the west.",
                         "locations": {"N": "Main Hallway", \
                                       "E": "Financial Department", \
                                        "S": "Parking Lot", \
                                            "W": "Supply Closet"}
                         }
            self.room_object = Room(self.room_file_name, self.room_json)

        def test_constructor(self):
            self.assertEqual(self.room_file_name, 
                             self.room_object.file_name)
            self.assertEqual(self.room_json['name'], 
                             self.room_object.name)
            self.assertEqual(self.room_json['description'], 
                             self.room_object.description)
            self.assertEqual(self.room_json['short_description'], 
                             self.room_object.short_description)
            self.assertEqual(self.room_json['items'], 
                             self.room_object.items)
            self.assertEqual(self.room_json['dropped_items'], 
                             self.room_object.dropped_items)
            self.assertEqual(self.room_json['directions'], 
                             self.room_object.directions)
            self.assertEqual(self.room_json['locations'], 
                             self.room_object.locations)
            
        def test_serialize_function(self):
            self.assertEqual(self.room_json, 
                             self.room_object
                             .serialize_as_json(self.room_object))


    class GameManagerClass(unittest.TestCase):
        def setUp(self):
            self.gm_const = GameManager()
            self.gm_inst = GameManager()
            self.player_file_name = 'player.json'
            self.player_json = {"name": "player", 
                           "inventory": ["item1"], 
                           "location": ["Reception Area"]}
            self.room_file_name = 'room1.json'
            self.room_json = {"name": "Reception Area",
                         "description": "Where you check in as a visitor",
                         "short_description": "Check in",
                         "items": [],
                         "dropped_items": [],
                         "directions": "The Reception Area is connected to " + 
                            "the Main Hallway to the north, the Financial " + 
                            "Department to the east, the Parking Lot to the " + 
                            "south and a Supply Closet to the west.",
                         "locations": {"N": "Main Hallway", 
                                       "E": "Financial Department", 
                                       "S": "Parking Lot", 
                                       "W": "Supply Closet"}
                         }

        def test_constructor(self):
            self.gm_const.cur_path = os.path.dirname(__file__)
            self.assertEqual(self.gm_const.player, None)
            self.assertEqual(self.gm_const.room_list, [])
            self.assertEqual(self.gm_const.item_list, [])
            self.assertEqual(self.gm_const.new_data_dirs, 
                             constants.NEW_DATA_DIRS)
            self.assertEqual(self.gm_const.saved_data_dirs, 
                             constants.SAVED_DATA_DIRS)
            
        def test_instanciated_new_obj_against_json_data(self):
            self.gm_inst.instantiate_objects()
            self.assertEqual(self.gm_inst.player.serialize_as_json(self
                                .gm_inst.player), 
                                self.player_json)
            self.assertEqual(self.gm_inst.room_list[0].serialize_as_json(self
                                .gm_inst.room_list[0]), self.room_json)
            
        def test_instanciated_saved_obj_against_json_data(self):
            self.gm_inst.instantiate_objects(load_saved_game = True)
            self.assertEqual(self.gm_inst.player.serialize_as_json(self
                                .gm_inst.player), 
                                self.player_json)
            self.assertEqual(self.gm_inst.room_list[0].serialize_as_json(self
                                .gm_inst.room_list[0]), self.room_json)


    unittest.main()
