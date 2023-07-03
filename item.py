from game_object import GameObject

class Item(GameObject):
    def __init__(self, item_data):
        super().__init__(item_data['name'])
        self.description = item_data['description']
        self.is_takeable = item_data['is_takeable']

    def to_string(self):
        print(self.name, self.description, self.is_takeable, sep='\n')
