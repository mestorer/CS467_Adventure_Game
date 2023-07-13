class LanguageLibrary:  
    def __init__(self):
        # defined language rules 
        self.language = {
            # Required verbs
            'look': ['at', 'target'], # can be used with or without target
            'go': ['location', 'location'], # exact location names always have two words
            'take': ['item'],
            'help': [],
            'inventory': [],
            'savegame': [],
            'loadgame': [],
            'quitgame': [],
            # Action verbs (not yet implemented)
            'use': ['item'], # need at least 9 more verbs
        }

        # all valid locations in the game
        self.locations = ['north', 'south', 'east', 'west', 
                    'n', 's', 'e', 'w',
                    'parking lot', 'reception area', 'supply closet', 'main hallway',
                    'it room', 'server room', 'executive elevator', 'executive office',
                    'marketing department', 'conference room', 'research lab', 'financial department',
                    'archives room']