from game_object import GameObject

class Room(GameObject):
    def __init__(self, room_data):
        super().__init__(room_data['name'])
        self.description = room_data['description']
        self.short_description = room_data['short_description']
        self.items = room_data['items']
        self.adjacent_rooms = room_data['adjacent_rooms']

if __name__ == '__main__':
    import os
    import json

    cur_path = os.path.dirname(__file__)
    new_rooms_path = cur_path + '/new_room_data/'
    saved_rooms_path = cur_path + '/saved_room_data/'
    room_files = []

    # Get all filenames in folder that end in 'json'
    for filename in os.scandir(new_rooms_path):
        if filename.is_file() and str(filename.path)[-4:] == 'json':
            file = filename.path.split('/')[-1]
            room_files.append(file)

    # Read all files and build room objects
    rooms_list = []
    # Build rooms from json file
    for room_file in room_files:
        with open(new_rooms_path + room_file, "r") as read_file:
            data = json.load(read_file)
        room = Room(data)
        rooms_list.append(room)

    # Save rooms
    for room in rooms_list:
        file_name = (room.name.replace(" ", "_") + '.json').lower()
        with open(saved_rooms_path + file_name, "w") as write_file:
            data = json.dump(room, write_file, 
                             default=room.serialize_as_json)
            