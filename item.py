from game_object import GameObject

class Item(GameObject):
    def __init__(self, file_name, item_data):
        super().__init__(file_name)
        self.name = item_data['name']
        self.description = item_data['description']
        self.use = item_data['use']
        self.is_takeable = item_data['is_takeable']
        self.combine = item_data['combine']
