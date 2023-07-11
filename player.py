from game_object import GameObject

class Player(GameObject):
    def __init__(self, file_name, player_data):
        super().__init__(file_name)
        self.name = player_data['name']
        self.inventory = player_data["inventory"]
        self.location = player_data["location"]
