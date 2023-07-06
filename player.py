from game_object import GameObject

class Player(GameObject):
    def __init__(self, player_data):
        super().__init__(player_data['name'])
        self.items = player_data["items"]
        self.location = player_data["location"]
