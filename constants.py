NEW_DATA_DIRS = ['/new_player_data/', '/new_room_data/', 
                 '/new_item_data/', '/new_door_data/']

SAVED_DATA_DIRS = ['/saved_player_data/', '/saved_room_data/', 
                   '/saved_item_data/', '/saved_door_data/']

# Terminal size
MIN_TERM_SIZE_COLS = 80
MIN_TERM_SIZE_LINES = 24 # useful for testing, increase later

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
Welcome, and good luck!'''

LINE_BREAK = '''
################################################################################ 
'''

RESULT_TEXT = {"bottle of match dust": "Using the rim of the plastic bottle, you scrape the heads of the matches into the opening.  The sulfur dust settles neatly onto the bottom.",
               "bottle of ammonia" : "You pour the ammonia into the plastic bottle.  The noxious fumes begin to make your eyes water before you quickly close the lid.",
               "stink bomb" : "You combine the items in the plastic bottle and quickly replace the lid, but not before you catch a whiff of the foul, gut-wrenching reaction occurring within.  This will undoubtedly clear any room.",
               "access card" : "You swipe the access card through the card reader.  The light turns green and the door unlocks with a click.",
               "deleted emails" : "You stick the flash drive into the first available port on the server rack. With your superior drag and drop skills, you are able to locate the missing emails from your coworker's computer and transfer them to the flash drive.",
               "compromising document" : "You look back and forth between the Executive's information and the safe, plugging in various dates, phone numbers - even his social security number - anything that could be used in some form as a combination.  When you try the date he started at the company, the door clicks loudly and squeaks open.  You wonder how much of a tool he really is."
               }

HELP_GUIDE = """                                   Help Guide
################################################################################
# look : look around the room you are in                                       #
#     Also try : l                                                             #
# look at <item>: look at the item in the room you are in or in your inventory #
#     Also try : inspect <item>, examine <item>                                #
# go <direction>: move in the direction specified                              #
#     Also try : <direction>                                                   #
# go <location>: move to the location specified                                #
#     Also try : <location>                                                    #
# take <item>: take the item specified                                         #
#     Also try : grab <item>                                                   #
# drop <item> : drop the item specified                                        #
# throw <item> : throw the item specified                                      #
#     Also try : toss <item>                                                   #
# use <item> : use the item specified                                          #
# use <item> on <item> : combine the two items specified                       #
#     Also try : combine <item> with <item>                                    #
# taste <item> : taste the item specified                                      #
#     Also try : lick <item>                                                   #
# touch <item> : touch the item specified                                      #
#     Also try : rub <item>, feel <item>                                       #
# smell <item> : smell the item specified                                      #
#     Also try : sniff <item>, inhale <item>                                   #
# shake <item> : shake the item specified                                      #
#     Also try : rock <item>                                                   #
# break <item> : break the item specified                                      #
#     Also try : smash <item>, crush <item>                                    #
# read <item> : read the item specified                                        #
# inventory : print the items in your inventory                                #
#     Also try : i                                                             #
# help : print this help guide                                                 #
#     Also try : h                                                             #
# savegame : save the game                                                     #
#     Also try : sg, save                                                      #
# loadgame : load the game                                                     #
#     Also try : lg, load                                                      #
# quitgame : quits the game                                                    #
#     Also try : qg, quit                                                      #
################################################################################"""
