from game_object import GameObject
from objects_mixin import ObjectsMixin
from ascii_art.item_art import ascii_art as art

class Item(GameObject, ObjectsMixin):
    def __init__(self, file_name, item_data):
        super().__init__(file_name)
        self.name = item_data['name']
        self.description = item_data['description']
        self.use = item_data['use']
        self.is_takeable = item_data['is_takeable']
        self.parent = item_data['parent']
        self.hints = item_data['hints']
        self.combine = item_data['combine']
        self.throw = item_data['throw']
        self.taste = item_data['taste']
        self.touch = item_data['touch']
        self.smell = item_data['smell']
        self.shake = item_data['shake']
        self.break_item = item_data['break_item']
        self.read = item_data['read']
        self.has_been_seen = False
        # If ASCII art exists, add it, if not, set it to None
        try:
            self.ascii_art = art[self.name]
        except:
            self.ascii_art = None
            
    def _remove_last_sentence(self, input_string):
        # Split the string into sentences using the period ('.') as the separator
        sentences = input_string.split('.')

        # Check if there is more than one sentence in the string
        if len(sentences) > 1:
            # Reconstruct the string without the last sentence
            result_string = '.'.join(sentences[:-2]).strip() + '.'
            return result_string
        else:
            # If there is only one sentence or no sentence, return the original string
            return input_string

            
    def remove_hints(self, item_list):
        if self.parent is not None:
            for item in self.parent:
                parent_obj = self._get_game_object_by_name(item, item_list)
                for attribute in parent_obj.hints:
                    current_value = getattr(parent_obj, attribute)
                    new_value = self._remove_last_sentence(current_value)
                    setattr(parent_obj, attribute, new_value)
                parent_obj.hints = []
                