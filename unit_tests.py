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
                           "location": "Reception Area"}
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
                         "items": ["key"],
                         "dropped_items": [],
                         "directions": "The Reception Area is connected to \
                            the Main Hallway to the north, the Financial \
                                Department to the east, the Parking Lot to the \
                                    south and a Supply Closet to the west.",
                         "locations": {"N": "Main Hallway", \
                                       "E": "Financial Department", \
                                        "S": "Parking Lot", \
                                            "W": "Supply Closet"},
                        "transitions": {},
                        "visited": False
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
            self.player_file_name = 'player.json'
            self.player_json = {"name": "player", 
                           "inventory": [], 
                           "location": "Reception Area"}
            self.room1_file_name = 'room1.json'
            self.room1_json = {
                        "name": "Reception Area",
                        "description": "Where you check in as a visitor",
                        "short_description": "Check in", 
                        "items": ["key"],
                        "dropped_items": [] ,
                        "directions": "The Test Room is connected to the Main Hallway to the north",
                        "locations": {"N": "Main Hallway"},
                        "transitions": {},
                        "visited": False
}
            self.room2_file_name = 'room2.json'
            self.room2_json = {
                        "name": "Main Hallway",
                        "description": "Where you check in as a visitor",
                        "short_description": "Check in", 
                        "items": ["id card"],
                        "dropped_items": [] ,
                        "directions": "The Main Hallway is connected to the Test Room to the south",
                        "transitions": {},
                        "locations": {"S": "Test Room 1"},
                        "visited": False
            }
            self.item1_file_name = 'item1.json'
            self.item1_json = {"name": "key",
                              "description": "a key that opens somtehing",
                              "is_takeable": True}
            self.item2_file_name = 'item2.json'
            self.item2_json = {"name": "id card",
                              "description": "a card that opens somtehing",
                              "is_takeable": True}

        def test_constructor(self):
            self.gm = GameManager()
            self.gm.cur_path = os.path.dirname(__file__)
            self.assertTrue(str(type(self.gm.parser)) 
                            == "<class 'nl_parser.NlParser'>")
            self.assertTrue(str(type(self.gm.command_processor)) 
                            == "<class 'command_processor.CommandProcessor'>")
            self.assertEqual(self.gm.player, None)
            self.assertEqual(self.gm.room_list, [])
            self.assertEqual(self.gm.item_list, [])
            self.assertEqual(self.gm.new_data_dirs, 
                             constants.NEW_DATA_DIRS)
            self.assertEqual(self.gm.saved_data_dirs, 
                             constants.SAVED_DATA_DIRS)
            
        def test_instanciated_new_obj_against_json_data(self):
            self.gm = GameManager()
            self.gm.new_data_dirs = ['/test_data/new_player_data/', 
                                     '/test_data/new_room_data/', 
                                     '/test_data/item_data/']
            self.gm.saved_data_dirs = ['/test_data/saved_player_data/', 
                                       '/test_data/saved_room_data/', 
                                       '/test_data/item_data/']
            self.gm.instantiate_objects()
            self.gm.player = Player(self.player_file_name, self.player_json)
            self.assertEqual(self.gm.player.serialize_as_json(self
                                .gm.player), 
                                self.player_json)
            self.assertEqual(self.gm.room_list[0].serialize_as_json(self
                                .gm.room_list[0]), self.room1_json)
            
        def test_instanciated_saved_obj_against_json_data(self):
            self.gm = GameManager()
            self.gm.new_data_dirs = ['/test_data/new_player_data/', 
                                     '/test_data/new_room_data/', 
                                     '/test_data/item_data/']
            self.gm.saved_data_dirs = ['/test_data/saved_player_data/', 
                                       '/test_data/saved_room_data/', 
                                       '/test_data/item_data/']
            self.gm.instantiate_objects(load_saved_game = True)
            self.gm.player = Player(self.player_file_name, self.player_json)
            self.assertEqual(self.gm.player.serialize_as_json(self
                                .gm.player), 
                                self.player_json)
            self.assertEqual(self.gm.room_list[0].serialize_as_json(self
                                .gm.room_list[0]), self.room1_json)
            
        def test_item_pick_up_by_player(self):
            self.gm = GameManager()
            self.gm.player = Player(self.player_file_name, self.player_json)
            room = Room(self.room1_file_name, self.room1_json)
            self.gm.room_list.append(room)
            room = Room(self.room2_file_name, self.room2_json)
            self.gm.room_list.append(room)
            item = Item(self.item1_file_name, self.item1_json)
            self.gm.item_list.append(item)
            item = Item(self.item2_file_name, self.item2_json)
            self.gm.item_list.append(item)
            self.gm.pick_up_item('key')
            self.assertEqual(self.gm.room_list[0].items, [])
            self.assertEqual(self.gm.player.inventory, ['key'])

        def test_item_drop_by_player(self):
            self.gm = GameManager()
            self.gm.player = Player(self.player_file_name, self.player_json)
            room = Room(self.room1_file_name, self.room1_json)
            self.gm.room_list.append(room)
            room = Room(self.room2_file_name, self.room2_json)
            self.gm.room_list.append(room)
            item = Item(self.item1_file_name, self.item1_json)
            self.gm.item_list.append(item)
            item = Item(self.item2_file_name, self.item2_json)
            self.gm.item_list.append(item)
            self.gm.pick_up_item('key')
            self.gm.drop_inventory_item_in_room('Reception Area', 'key')
            self.assertEqual(self.gm.room_list[0].dropped_items, ['key'])
            self.assertEqual(self.gm.player.inventory, [])

        def test_move_player_to_new_room(self):
            self.gm = GameManager()
            self.gm.player = Player(self.player_file_name, self.player_json)
            room = Room(self.room1_file_name, self.room1_json)
            self.gm.room_list.append(room)
            room = Room(self.room2_file_name, self.room2_json)
            self.gm.room_list.append(room)
            item = Item(self.item1_file_name, self.item1_json)
            self.gm.item_list.append(item)
            item = Item(self.item2_file_name, self.item2_json)
            self.gm.item_list.append(item)
            self.gm.move_player_to_new_roow(self.room2_json["name"])
            self.assertEqual(self.room2_json["name"], self.gm.player.location)
            

    unittest.main()
