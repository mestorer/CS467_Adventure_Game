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

GAME_OUTRO = '''
You're finally free of the corporate world. You're free of the endless
meetings, the petty politics, the backstabbing, the gossip, the drama, the
emails, the pointless projects, the micromanaging, the soul-crushing
boredom, the... You're free!'''

SCORE_RESULTS = {
  "A": "Congratulations! You have demonstrated exceptional skills and dedication throughout the game. Your performance has been truly remarkable, and you've consistently exceeded expectations. Keep up the outstanding work, and you'll continue to be a valuable asset to the team.",
  "B": "You've shown great competence and a strong work ethic in this corporate challenge. While there's room for improvement, your performance has been commendable. Continue to focus on enhancing your skills and taking initiative to reach new heights in your game endeavors.",
  "C": "You've met the basic requirements and completed the game with an acceptable level of competence. Your performance has been satisfactory, but there's still room for growth. Use this experience as a stepping stone to refine your abilities and contribute more effectively in future tasks.",
  "D": "Your performance in the game has been inconsistent, and there are areas where improvement is required. Pay attention to the feedback provided, identify your weaknesses, and work diligently to enhance your skills. With determination and effort, you can turn things around and achieve better results.",
  "F": "Unfortunately, your performance fell short of expectations. Your lack of engagement and effort has been evident throughout the game. Take this as a valuable learning experience and use it to assess your strengths and weaknesses. Set specific goals to improve your skills and make a comeback in future challenges."
}

LINE_BREAK = '''
################################################################################ 
'''

RESULT_TEXT = {"bottle of match dust": "Using the rim of the plastic bottle, you scrape the heads of the matches into the opening.  The sulfur dust settles neatly onto the bottom.",
               "bottle of ammonia" : "You pour the ammonia into the plastic bottle.  The noxious fumes begin to make your eyes water before you quickly close the lid.",
               "stink bomb" : "You combine the items in the plastic bottle and quickly replace the lid, but not before you catch a whiff of the foul, gut-wrenching reaction occurring within.  This will undoubtedly clear any room.",
               "access badge" : "You swipe the access card through the card reader.  The light turns green and the door unlocks with a click.",
               "deleted emails" : "You stick the flash drive into the first available port on the server rack. With your superior drag and drop skills, you are able to locate the missing emails from your coworker's computer and transfer them to the flash drive.",
               "confidential information" : "You look back and forth between the Executive's information and the safe, plugging in various dates, phone numbers - even his social security number - anything that could be used in some form as a combination.  When you try the date he started at the company, the door clicks loudly and squeaks open.  You wonder how much of a tool he really is."
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

STORY_MOMENTS = {
    "1": """Shutting off the engine to your car, you take a deep breath, pop
     open the door and hop out, accidentally shutting the door behind you with
     a little too much force. You can physically feel the anticipation and
     dread filling your chest. "Get down here now" – you can still hear your
     colleague's words echoing in your mind. "Something big happened and it
     looks like you might be in trouble."

    You should head to your desk in marketing as soon as possible and find
     out what is going on.
    """,
    "2": """As your eyes scan farther down the discipline notice, each new
     line leaves you with more questions than answers. You work in marketing.
     You're not terribly fond of your job but it pays the bills, and your
     performance is a testament to this.  This notice, however, is saying
     that you ordered exorbitantly overpriced advertisement packages from
     a company you've never heard of, and finance flagged the transaction.
     The notice closes with a dread-inducing warning that an investigation
     is underway.  You should stop by your [coworker's desk] in finance to
     find out more.
    """,
    "3": """With anxiety rising in your chest, you quickly glance between
     the emails and the meeting notes. The confusion mounting in your mind
     slowly begins to resolve into a terrible combination of fear and anger.
     Pieces aren't lining up.  You know you had nothing to do with the initial
     transaction, and now it looks like someone is actively poking holes in
     whatever trail could be followed to the actual culprit.  You feel like
     there might be some more answers back at your coworker's desk if you dig
     a little deeper.
    """,
    "4": """The emails immediately allay some of your fears and stir up
     considerable righteous fury.  Messages between your finance coworker
     detail some of the initial investigation's fact-finding and an abrupt
     order to desist immediately.  You don't recognize the author
     of the order, but it is readily apparent that your coworker does.  It has
     become painfully clear to you that some shady business practices are
     underway and someone had no qualms about throwing you under the bus if
     they ever came to light.

    Now that you have some damning and direct evidence, you're ready to take
     this to the top:  You need to get this to the CEO himself and clear your
     name before this goes too far.
    """,
    "50": """Looking at the bottle of match dust in your hand, you know
     you have half of a room-clearing prank.  Now you just need to find the
     chemical counterpart.  The lab has a plethora of various chemicals,
     perhaps you can find something there.
    """,
    "51": """Looking at the bottle of foul ammonia in your hand, you know
     you have half of a room-clearing prank.  Now you just need to find
     something with some type of sulfur, and nothing in the lab seems to
     fit the bill. The supply closet is probably the next place to check out.
    """,
    "6": """You look at the bottle in your hand again.  This time, you feel
     the slightest tinge of remorse for what you're about to release
     on the receptionist.  She's always been pleasant, if perhaps a bit strict.
     Regardless, you have a mission and you're going to see it through...even
     if it means ruining that poor lady's sense of smell for a couple weeks.
    """,
    "7": """You pull the keycard up to your eyes.  Nothing physically changed,
     but you feel a sense of power emanating from it.  This will get you up
     the elevator and into the CEO's office.  Time to get some answers.
    """,
    "8": """You can't help but feel a bit deflated.  Every time you think
     you're about to find some answers, you're met with another heap of
     questions. Looking between the papers on the desk and the safe, you
     can't help but feel the weight of your intuition and what it's
     suggesting.  You need to get into that safe, and the combination doesn't
     appear to be anywhere around here.  You have the key to the archives...
     perhaps you can find something – anything – that the CEO might have used
     as a combination in his personal records.""",
    "9": """Scanning through the CEO's personal information, you're met with
     a wide collection of numbers ...phone numbers, significant dates like
     the CEO's birthday, and even the first day PrestoCorp started operations.
     You feel somewhat confident that something here could be the combination
     to that safe.""",
    "10": """You read line by line down the CEO's file, rolling the dial
     backwards and forwards as you try each number in turn.  Finally, as your
     hope begins to wane, the lock makes an audible click and the handle shakes
     slightly.  You hesitantly grip the handle and rotate it, and it gives no
     resistance.  With your hope renewed, you swing open the door in triumph...
     and are met with surprisingly little. [NL]

    One folder rests at the bottom of the safe.  You snatch it and open it
     quickly.  The small amount of frustration that had begun rising
     immediately vanishes.  This is it.  This is your answer. [NL]

    Reading down the first document answers your original question of 'who?'.
     It is a detailed list of transactions to almost comically bland business
     names like AdvertCorp  and Initech. It was the CEO himself that set up
     the fraudulent transaction.  And multiple others. It's been ongoing for
     years.  And the transaction amounts have ballooned over that time.  Based
     off the name of the company in the discipline notice, the transaction made
     under your name is substantially larger than any of the previous.  It's
     clear why finance flagged this transaction…it's a little less clear how
     the rest of these weren't caught. [NL]

    That question doesn't linger long in your mind as you move to the next
     page. It's a collection of messages to and from your finance coworker...
     the CEO was the one that ordered your coworker to drop the investigation.
     This definitively answers 'why?'.  The CEO is also the owner.  Well,
     founder and majority owner.  He's been defrauding the other investors by
     moving a portion of the company's profits into what you assume are shell
     businesses he owns. [NL]

    Conveniently – although it did take some work to get here – the CEO has
     handed you the smoking gun on a silver platter between the correspondence
     and the transaction ledger.  You need to get out and get this to the
     authorities immediately.  You can't be sure how many of the previous
     transactions were falsely made under your authority or any other innocent
     victim. [NL]

    The elevator ride down is a blur. You can't believe you've made it this
     far and found the truth.  But quickly, the realization strikes you…
    """
}
