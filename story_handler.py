from helper_functions import print_text, print_slowly
import constants

class StoryHandler:
    def __init__(self):
        self.story = {
            "1": "Story #1: Start of game upon entering parking lot. Hint at going to my desk in marketing",
            "2": "Story #2: Caused by taking notice of disciplinary action. Hint at coworker's desk in finance.",
            "3": "Story #3: Caused by having suspicous email and meeting notes in inventory. Hint at returning to coworker's desk in finance.",
            "4": "Story #4: Caused by crafting the deleted emails. Tell player to take these documents to CEO.",
            "5": "Story #5: Caused by crafting the bottle of match dust or bottle of ammonia. Tell player that they can probably turn this into a stink bomb to clear the lobby if they find another component.",
            "6": "Story #6: Caused by crafting the stink bomb. Tell player to go to the lobby and use the stink bomb to clear it out.",
            "7": "Story #7: Caused by crafting the access badge. Tell player they can now go see the CEO in the executive office.",
            "8": "Story #8: Caused by taking the CEO's silver key. Tell player something fishy is afoot and they should check the archives to solve the mystery.",
            "9": "Story #9: Caused by taking personal information from archives. Tell player to use personal info to open CEO safe.",
            "10": "Story #10: Caused by taking the confidential information from safe. End game story here."
        }

    def _get_game_object_by_name(self, name, obj_list):
        """
        Returns the actual game object with the matching name attribute or
        None if there's no match.
        """
        for obj in obj_list:
            if obj.name == name:
                return obj
            
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
            player.checkpoint = 5 #can include a different checkpoint for each conditional if we want diff text for each
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