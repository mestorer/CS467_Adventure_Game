from game_object import GameObject

class Player(GameObject):
    def __init__(self, file_name, player_data):
        super().__init__(file_name)
        self.name = player_data['name']
        self.inventory = player_data["inventory"]
        self.location = player_data["location"]
        self.checkpoint = player_data["checkpoint"]
        self.prev_checkpoint = player_data["prev_checkpoint"]
        self.item_flags = player_data["item_flags"]
        self.total_score = player_data["total_score"]