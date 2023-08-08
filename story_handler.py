from helper_functions import print_text
from objects_mixin import ObjectsMixin
import constants

class StoryHandler(ObjectsMixin()):
    def __init__(self):
        self.story = constants.STORY_MOMENTS
            
    def _display_story(self, player):
        """
        Displays the story text for the player's current checkpoint.
        """
        checkpoint = str(player.checkpoint)
        if checkpoint in self.story:
            print_text(self.story[checkpoint], color=constants.colors.GREEN, pause=0.025)
            # if we pass other objects into this function we can modify other aspects of the game!
            
    # should add ability to check is_locked on Door objects
    def _advance_checkpoint(self, player, item_list):
        """
        Advances the player's checkpoint attribute if they have met the requirements.
        """
        if "notice of disciplinary action" in player.item_flags:
            player.checkpoint = 2
            player.item_flags.remove("notice of disciplinary action")   # remove item from flags so story doesn't repeat
        elif "suspicious email" in player.item_flags and "meeting notes" in player.item_flags:
            player.checkpoint = 3
            player.item_flags.remove("suspicious email")
            player.item_flags.remove("meeting notes")
            cw_desk = self._get_game_object_by_name("coworker's desk", item_list)
            cw_desk.description = "Here is a hint that points the player to explore the server room to acquire missing emails."
        elif "deleted emails" in player.item_flags:
            player.checkpoint = 4
            player.item_flags.remove("deleted emails")
        elif ("bottle of match dust" in player.item_flags or "bottle of ammonia" in player.item_flags):
            # different checkpoint based on which half is acquired first
            player.checkpoint = 50 if "bottle of match dust" in player.item_flags else 51
            if "bottle of match dust" in player.item_flags:
                player.item_flags.remove("bottle of match dust")
            else:
                player.item_flags.remove("bottle of ammonia")
        elif "stink bomb" in player.item_flags:
            player.checkpoint = 6
            player.item_flags.remove("stink bomb")
        elif "access badge" in player.item_flags:
            player.checkpoint = 7
            player.item_flags.remove("access badge")
        elif "silver key" in player.item_flags:
            player.checkpoint = 8
            player.item_flags.remove("silver key")
        elif "personal information" in player.item_flags:
            player.checkpoint = 9
            player.item_flags.remove("personal information")
        elif "confidential information" in player.item_flags:
            player.checkpoint = 10
            player.item_flags.remove("confidential information")
            #insert end game function from game_manager here

    def check_story(self, player, item_list):
        """
        Checks if the player has reached a new checkpoint and displays the appropriate story text.
        """
        self._advance_checkpoint(player, item_list)
        if player.checkpoint != player.prev_checkpoint:
            self._display_story(player)
            player.prev_checkpoint = player.checkpoint