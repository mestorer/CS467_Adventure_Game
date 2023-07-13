from game_object import GameObject

class Room(GameObject):
    def __init__(self, file_name, room_data):
        super().__init__(file_name)
        self.name = room_data['name']
        self.description = room_data['description']
        self.short_description = room_data['short_description']
        self.items = room_data['items']
        self.dropped_items = room_data['dropped_items']
        self.directions = room_data['directions']
        self.locations = room_data['locations']
        self.doors = room_data['doors']
        self.visited = room_data['visited']
