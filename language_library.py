class LanguageLibrary:  
    def __init__(self):
        # defined language rules
        self.language = {
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
            # aliases
            'l': [], # look
            'inspect': ['item'], # look at target
            'examine': ['item'], # look at target
            'grab': ['item'], # take item
            'h': [], # help
            'i': [], # inventory
            'sg': [], # save game
            'save': [], # save game
            'lg': [], # load game
            'load': [], # load game
            'qg': [], # quit game
            'quit': [], # quit game
            'combine': ['item', 'with', 'item'], # use item on item
            'toss': ['item'], # throw item
            'lick': ['item'], # taste
            'rub': ['item'], # touch
            'feel': ['item'], # touch
            'sniff': ['item'], # smell
            'inhale': ['item'], # smell
            'rock': ['item'], # shake
            'smash': ['item'], # break
            'crush': ['item'], # break
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
