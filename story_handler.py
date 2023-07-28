from helper_functions import print_text, print_slowly
import constants

class StoryHandler:
    def __init__(self):
        self.story = {
            "1": "Welcome to your adventure! Get ready to experience a world of working for a corporation where you are nothing but a number. Enjoy your day!",
            "2": "You have always wanted a key to the lab. You have always wanted to play with all the chemicals and machines that are in there. Now is your chance! Get in there and cause some trouble!",
            "3": "Ammonia and a blank keycard. What could you possibly do with these? You have no idea, but you are sure you will think of something.",
        }

    def _display_story(self, player):
        """
        Displays the story text for the player's current checkpoint.
        """
        checkpoint = str(player.checkpoint)
        if checkpoint in self.story:
            print_text(self.story[checkpoint], color=constants.colors.GREEN, pause=0.025)
            # if we pass other objects into this function we can modify other aspects of the game!
        else:
            print_text("The story is over I guess... STORY MISSING", color=constants.colors.GREEN, pause=0.025)
            
    # should add ability to check is_locked on Door objects
    def _advance_checkpoint(self, player):
        """
        Advances the player's checkpoint attribute if they have met the requirements.
        """
        if "lab key" in player.item_flags:
            player.checkpoint += 1
            player.item_flags.remove("lab key")   # remove item from flags so story doesn't repeat
        elif "ammonia" in player.item_flags and "blank keycard" in player.item_flags:
            player.checkpoint += 1
            player.item_flags.remove("ammonia")
            player.item_flags.remove("blank keycard")
        # add more checkpoints here
        
    def recap_story(self, player):
        """
        Recap the last story message displayed to player.
        """
        print_text("Recap: ")
        self._display_story(player)

    def check_story(self, player):
        """
        Checks if the player has reached a new checkpoint and displays the appropriate story text.
        """
        self._advance_checkpoint(player)
        if player.checkpoint != player.prev_checkpoint:
            self._display_story(player)
            player.prev_checkpoint = player.checkpoint