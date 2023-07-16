from game_object import GameObject

class Door(GameObject):
    def __init__(self, file_name, data):
        super().__init__(file_name)
        self.name = data['name']
        self.is_locked = data['is_locked']  # Initial state of the door
        self.locked_message = data['locked_message']
        self.unlocked_after_key_message = data['unlocked_after_key_message']
        self.unlocked_message = data['unlocked_message']
        # 'key' is the item that unlocks the transition to the next room
        self.key = data['key']

    def try_open_door(self, player):
        move_player = True
        if self.is_locked and not self.key in player.inventory:
            message = self.locked_message
            move_player = False
        elif self.is_locked and self.key in player.inventory:
            message = self.unlocked_after_key_message
            self.is_locked = False
        else:
            message = self.unlocked_message
        return move_player, message