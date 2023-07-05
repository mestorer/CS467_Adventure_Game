from game_object import GameObject

class Room(GameObject):
    def __init__(self, room_data):
        super().__init__(room_data['name'])
        self.description = room_data['description']
        self.short_description = room_data['short_description']
        self.items = room_data['items']
        self.adjacent_rooms = room_data['adjacent_rooms']
