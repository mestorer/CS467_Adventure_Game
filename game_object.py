class GameObject:
    def __init__(self, file_name):
        self.file_name = file_name

    def serialize_as_json(self, obj_json):
        """
        Serializes all attributes as JSON to save as a JSON
        formatted text file
        """
        attributes = vars(obj_json)
        attributes.pop("file_name")
        return attributes
    
    def to_string(self):
        """
        Prints all the attributes and their values as a string
        separated by a new line 
        """
        [print(key,':',vars(self)[key]) for key in vars(self)]