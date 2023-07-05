from game_object import GameObject

class Item(GameObject):
    def __init__(self, item_data):
        super().__init__(item_data['name'])
        self.description = item_data['description']
        self.is_takeable = True if item_data['is_takeable'] == 'True' else False
