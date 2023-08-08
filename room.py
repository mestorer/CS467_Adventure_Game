from game_object import GameObject
from ascii_art.room_art import ascii_art as art

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
        # If ASCII art exists, add it, if not, set it to None
        try:
            self.ascii_art = art[self.name]
        except:
            self.ascii_art = None

    def describe(self, long_desc=False):
        '''
        Returns a list of messages that describe the room'''
        messages = []
        if long_desc or not self.visited:
            messages.append(self.description)
        else:
            messages.append(self.short_description)
        if self.dropped_items != []:
            messages.append(f"You see the following items scattered about \
                       on the floor: {self.dropped_items}")
        messages.append(self.directions + '\n')
        return messages

    def mark_as_visited(self):
        self.visited = True
