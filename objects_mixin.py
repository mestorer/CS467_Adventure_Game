import sys

class ObjectsMixin:
    def _get_game_object_by_name(self, name, obj_list):
        """
        Returns the actual game object with the matching name attribute or
        None if there's no match.
        """
        for obj in obj_list:
            if obj.name == name:
                return obj
            
    def clear_screen(self):
        sys.stdout.write("\033[2J")
        sys.stdout.write("\033[H")