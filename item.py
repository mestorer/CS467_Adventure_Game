from game_object import GameObject

class Item(GameObject):
    def __init__(self, file_name, item_data):
        super().__init__(file_name)
        self.name = item_data['name']
        self.description = item_data['description']
        self.use = item_data['use']
        self.is_takeable = item_data['is_takeable']
        self.combine = item_data['combine']
        self.throw = item_data['throw']
        self.taste = item_data['taste']
        self.touch = item_data['touch']
        self.smell = item_data['smell']
        self.shake = item_data['shake']
        self.break_item = item_data['break_item']
        self.read = item_data['read']