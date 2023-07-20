class LanguageLibrary:  
    def __init__(self):
        # defined language rules
        self.language = {
            # Required verbs
            'look': ['at', 'target'],  # can be used with or without target
            'go': ['location', 'location'],
            'take': ['item'],
            'help': [],
            'inventory': [],
            'savegame': [],
            'loadgame': [],
            'quitgame': [], 
            'use': ['item', 'on', 'item'], # can be used as 'use item' or 'use item on item',
            'drop': ['item'],
            'throw' : ['item'],
            'taste' : ['item'],
            'touch' : ['item'],
            'smell' : ['item'],
            'shake' : ['item'],
            'break' : ['item'],
            'read' : ['item'],
        }

        # all valid locations in the game
        self.locations = ['north', 'south', 'east', 'west',
                          'n', 's', 'e', 'w',
                          'parking lot', 'parking', 'lot',
                          'reception area', 'reception',
                          'supply closet', 'supply', 'closet'
                          'main hallway', 'hallway',
                          'it room', 'it',
                          'server room', 'server',
                          'executive elevator', 'elevator',
                          'executive office', 'executive', 'office',
                          'marketing department', 'marketing',
                          'conference room', 'conference'
                          'research lab', 'research', 'lab'
                          'financial department', 'financial', 'finance',
                          'archives room', 'archives', 'archive']
