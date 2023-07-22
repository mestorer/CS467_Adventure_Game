NEW_DATA_DIRS = ['/new_player_data/', '/new_room_data/', 
                 '/new_item_data/', '/new_door_data/']

SAVED_DATA_DIRS = ['/saved_player_data/', '/saved_room_data/', 
                   '/saved_item_data/', '/saved_door_data/']

# Terminal size
MIN_TERM_SIZE_COLS = 80
MIN_TERM_SIZE_LINES = 24

# Terminal text colors
class colors:
  PURPLE = '\033[95m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ENDCOLOR = '\033[0m'
  NOCOLOR = '\033[0m'

OPENING_TITLE = '''
  _____                                          _         
 / ____|                                        | |        
| |       ___   _ __  _ __    ___   _ __   __ _ | |_   ___ 
| |      / _ \ | '__|| '_ \  / _ \ | '__| / _` || __| / _ \\
| |____ | (_) || |   | |_) || (_) || |   | (_| || |_ |  __/
 \_____| \___/ |_|   | .__/  \___/ |_|    \__,_| \__| \___|
                     | |                                   
                     |_|                                   
  _____                            _                           
 / ____|                          (_)                          
| |       ___   _ __   ___  _ __   _  _ __   __ _   ___  _   _ 
| |      / _ \ | '_ \ / __|| '_ \ | || '__| / _` | / __|| | | |
| |____ | (_) || | | |\__ \| |_) || || |   | (_| || (__ | |_| |
 \_____| \___/ |_| |_||___/| .__/ |_||_|    \__,_| \___| \__, |
                           | |                            __/ |
                           |_|                           |___/ 

                           
OSU Capstone Project: Garrett Crowley, Sean Tyler, Michael Estorer
                           
'''

GAME_INTRO = '''
Welcome to "Corporate Conspiracy"!\n
In the mundane world of PrestoCorp, you are just an ordinary office worker, 
but your patience is wearing thin. Dealing with the never-ending demands of 
your overbearing boss and navigating the treacherous corporate politics is 
draining your enthusiasm.\n
But today is different. As you enter the parking lot, you decide it's time 
for a change. Your goal is simple—avoid getting fired at all costs. You've 
had enough of being a pawn in the corporate game, and now it's time to take
matters into your own hands.\n
As you head to your desk in the Marketing Department, you discover a dreaded 
"Notice of Disciplinary Action" waiting for you. Your heart races as you wonder 
who might be trying to sabotage you and how you can turn the tables on them.\n
Welcome, and good luck!
'''

RESULT_TEXT = {"bottle of match dust": "Using the rim of the plastic bottle, you scrape the heads of the matches into the opening.  The sulfur dust settles neatly onto the bottom.",
               "bottle of ammonia" : "You pour the ammonia into the plastic bottle.  The noxious fumes begin to make your eyes water before you quickly close the lid.",
               "stink bomb" : "You combine the items in the plastic bottle and quickly replace the lid, but not before you catch a whiff of the foul, gut-wrenching reaction occurring within.  This will undoubtedly clear any room.",
               "access card" : "You swipe the access card through the card reader.  The light turns green and the door unlocks with a click.",
               "compromising document" : "You look back and forth between the Executive's information and the safe, plugging in various dates, phone numbers - even his social security number - anything that could be used in some form as a combination.  When you try the date he started at the company, the door clicks loudly and squeaks open.  You wonder how much of a tool he really is."
               }

HELP_GUIDE = """-----------------------------------Help Guide-----------------------------------
look: look around the room you are in
look at <item>: look at the item in the room you are in or in your inventory
go <direction>: move in the direction specified
<direction>: move in the direction specified
go <location>: move to the location specified
<location>: move to the location specified
take <item>: take the item specified
drop <item>: drop the item specified
throw <item>: throw the item specified
use <item>: use the item specified
use <item> on <item>: combine the two items specified
taste <item>: taste the item specified
touch <item>: touch the item specified
smell <item>: smell the item specified
shake <item>: shake the item specified
break <item>: break the item specified
read <item>: read the item specified
inventory: print the items in your inventory
help: print this help guide
savegame: save the game
loadgame: load the game
quitgame: quits the game\n"""

door_approaching = [
  """     
     ___
    |  .|
    |___|
  """,
  """     
     ____
    |    |
    |   .|
    |____|
  """,
  """     
     _____
    |     |
    |     |
    |    o|
    |     |
    |_____|
  """,
  """     
    _______
   |       |
   |       |
   |       |
   |      O|
   |       |
   |       |
   |_______
  """,
    """     
   _________
  |         |
  |         |
  |         |
  |         |
  |       O |
  |         |
  |         |
  |         |
  |_________|
  """
]

door_at = [
            """     
   _________
  |         |
  |         |
  |         |
  |         |
  |       O |
  |         |
  |         |
  |         |
  |_________|
  """
]

door_opening = [
"""    
   _________
  |         |
  |         |
  |         |
  |         |
  |       O |
  |         |
  |         |
  |         |
  |_________|
  """,
"""    
   _________
  |        ||
  |        ||
  |        ||
  |        ||
  |      O ||
  |        ||
  |        ||
  |        ||
  |________||
  """,
"""    
   _________
  |       | |
  |       | |
  |       | |
  |       | |
  |     O | |
  |       | |
  |       | |
  |       | |
  |_______|_|
  """,
"""    
   _________
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |    O |  |
  |      |  |
  |      |  |
  |      |  |
  |______|__|
  """,
"""    
   _________
  |     |   |
  |     |   |
  |     |   |
  |     |   |
  |   O |   |
  |     |   |
  |     |   |
  |     |   |
  |_____|___|
  """,
"""    
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |   O|    |
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """,
"""    
   _________
  |   |     |
  |   |     |
  |   |     |
  |   |     |
  |  o|     |
  |   |     |
  |   |     |
  |   |     |
  |___|_____|
  """,
"""    
   _________
  |  |      |
  |  |      |
  |  |      |
  |  |      |
  | o|      |
  |  |      |
  |  |      |
  |  |      |
  |__|______|
  """,
"""    
   _________
  | |       |
  | |       |
  | |       |
  | |       |
  |.|       |
  | |       |
  | |       |
  | |       |
  |_|_______|
  """,
"""    
   _________
  | |       |
  | |       |
  | |       |
  | |       |
  |.|       |
  | |       |
  | |       |
  | /       |
  |/________|
  """,
  """     
   _________
  | |       |
  | |       |
  | |       |
  |/        |
  ||        |
  ||        |
  |/        |
  |         |
  |_________|
  """,
  """     
   _________
  | |       |
  | |       |
  | |       |
  | /       |
  |/        |
  |         |
  |         |
  |         |
  |_________|
  """,
  """     
   _________
  | /       |
  ||        |
  |/        |
  |         |
  |         |
  |         |
  |         |
  |         |
  |_________|
  """,
        """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |_________|
  """
]

door_open =[
                """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |_________|
  """
]

elevator_approaching = [
  """     
   

  
     ___
    | | |
    |_|_|
  """,
  """     
   
  
  
     ___
    | | |
    | | | .
    |_|_|
  """,
  """     
   
  
     _____
    |  |  |
    |  |  |
    |  |  | o
    |  |  |
    |__|__|
  """,
  """     
   
    _______
   |   |   |
   |   |   |
   |   |   |
   |   |   | []
   |   |   |
   |   |   |
   |___|___|
  """,
  """     
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    | []
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """
]

elevator_at = [
          """     
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    | []
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """
]

elevator_opening = [
  """     
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    | []
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """,
  """     
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |    |    | []
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """,
  """     
   _________
  |   | |   |
  |   | |   |
  |   | |   |
  |   | |   |
  |   | |   | []
  |   | |   |
  |   | |   |
  |   | |   |
  |___|_|___|
  """,
  """     
   _________
  |  |   |  |
  |  |   |  |
  |  |   |  |
  |  |   |  |
  |  |   |  | []
  |  |   |  |
  |  |   |  |
  |  |   |  |
  |__|___|__|
  """,
  """     
   _________
  | |     | |
  | |     | |
  | |     | |
  | |     | |
  | |     | | []
  | |     | |
  | |     | |
  | |     | |
  |_|_____|_|
  """,
  """     
   _________
  ||       ||
  ||       ||
  ||       ||
  ||       ||
  ||       || []
  ||       ||
  ||       ||
  ||       ||
  ||_______||
  """,
        """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         | []
  |         |
  |         |
  |         |
  |_________|
  """
]

elevator_open = [
                """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         | []
  |         |
  |         |
  |         |
  |_________|
  """
]

door_badge_approaching = [
  """     
   

  
     ___
    |  .|
    |___|
  """,
  """     
   
  
  
     ____
    |    |
    |   .| .
    |____|
  """,
  """     
   
  
     _____
    |     |
    |     |
    |    o| o
    |     |
    |_____|
  """,
  """     
   
    _______
   |       |
   |       |
   |       |
   |      O| []
   |       |
   |       |
   |_______|
  """,
    """     
   _________
  |         |
  |         |
  |         |
  |         |
  |       O | []
  |         |
  |         |
  |         |
  |_________|
  """
]

door_badge_at = [
            """     
   _________
  |         |
  |         |
  |         |
  |         |
  |       O | []
  |         |
  |         |
  |         |
  |_________|
  """
]

door_badge_opening = [
  """    
   _________
  |         |
  |         |
  |         |
  |         |
  |       O | []
  |         |
  |         |
  |         |
  |_________|
  """,
  """    
   _________
  |        ||
  |        ||
  |        ||
  |        ||
  |      O || []
  |        ||
  |        ||
  |        ||
  |________||
  """,
  """    
   _________
  |       | |
  |       | |
  |       | |
  |       | |
  |     O | | []
  |       | |
  |       | |
  |       | |
  |_______|_|
  """,
  """    
   _________
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |    O |  | []
  |      |  |
  |      |  |
  |      |  |
  |______|__|
  """,
  """    
   _________
  |     |   |
  |     |   |
  |     |   |
  |     |   |
  |   O |   | []
  |     |   |
  |     |   |
  |     |   |
  |_____|___|
  """,
  """    
   _________
  |    |    |
  |    |    |
  |    |    |
  |    |    |
  |   O|    | []
  |    |    |
  |    |    |
  |    |    |
  |____|____|
  """,
  """    
   _________
  |   |     |
  |   |     |
  |   |     |
  |   |     |
  |  o|     | []
  |   |     |
  |   |     |
  |   |     |
  |___|_____|
  """,
  """    
   _________
  |  |      |
  |  |      |
  |  |      |
  |  |      |
  | o|      | []
  |  |      |
  |  |      |
  |  |      |
  |__|______|
  """,
  """    
   _________
  | |       |
  | |       |
  | |       |
  | |       |
  |.|       | []
  | |       |
  | |       |
  | |       |
  |_|_______|
  """,
  """    
   _________
  | |       |
  | |       |
  | |       |
  | |       |
  |.|       | []
  | |       |
  | |       |
  | /       |
  |/________|
  """,
  """     
   _________
  | |       |
  | |       |
  | |       |
  |/        |
  ||        | []
  ||        |
  |/        |
  |         |
  |_________|
  """,
  """     
   _________
  | |       |
  | |       |
  | |       |
  | /       |
  |/        | []
  |         |
  |         |
  |         |
  |_________|
  """,
  """     
   _________
  | /       |
  ||        |
  |/        |
  |         |
  |         | []
  |         | 
  |         |
  |         |
  |_________|
  """,
        """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         | []
  |         |
  |         |
  |         |
  |_________|
  """
]

door_badge_open = [
                """     
   _________
  |         |
  |         |
  |         |
  |         |
  |         | []
  |         |
  |         |
  |         |
  |_________|
  """
]
