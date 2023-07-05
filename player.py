from game_object import GameObject

class Player(GameObject):
    def __init__(self, player_data):
        super().__init__(player_data['name'])
        self.items = []
        self.location = []

if __name__ == '__main__':
    import os
    import json

    cur_path = os.path.dirname(__file__)
    new_player_path = cur_path + '/new_player_data/'
    saved_player_path = cur_path + '/saved_player_data/'
    
    # Read player file and build player object
    # Build player from json file
    player_file = 'player.json'
    with open(new_player_path + player_file, "r") as read_file:
        data = json.load(read_file)
    player = Player(data)

    # Save player
    file_name = (player.name.replace(" ", "_") + '.json').lower()
    with open(saved_player_path + file_name, "w") as write_file:
        data = json.dump(player, write_file, 
                         default=player.serialize_as_json)
         