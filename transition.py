from game_object import GameObject

class Transition(GameObject):
    def __init__(self, file_name, data):
        super().__init__(file_name)
        self.name = data['name']
        self.is_locked = data['locked']  # Initial state of the door
        self.locked_message = data['locked_message']
        self.unlocked_message = data['unlocked_message']
        # 'key' is the item that unlocks the transition to the next room
        self.key = data['key']
