class GameObject:
    def __init__(self, name):
        self.name = name

    def serialize_as_json(self, room_json):
        """
        Serializes all attributes as JSON to save as a JSON
        formatted text file"""
        attributes = vars(room_json)
        json_formatted_att = {}
        for attribute in attributes:
            json_formatted_att[attribute] = attributes[attribute]
        return json_formatted_att