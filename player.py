from game_object import GameObject

class Player(GameObject):
    def __init__(self, file_name, player_data):
        super().__init__(file_name)
        self.name = player_data['name']
        self.items = player_data["items"]
        self.location = player_data["location"]
