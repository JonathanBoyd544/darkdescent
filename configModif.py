# -*- coding: utf-8 -*-
"""
Read and process configuration files for labyrinth.

TODO:
    define data structures
    read csv
    ignore heading line
    process column data into internal data structure

Future improvements:
    maintain configuration file as JSON to facilitate easier import
        
Done:
    Not much yet. 
"""

import os
import sys

import random
from random import randint
import numpy as np
from configparser import ConfigParser
import time
import time
from tqdm import tqdm, trange
# import pandas as pd
# from progress.bar import Bar




verbosity = 6
incamount = 0
playerLvl = 0
xpForLevel = 50
tof = "true"
class Player:
    def __init__(self):
        self.level = 0
        self.maxhealth = 100
        self.health = self.maxhealth
        self.damageMulti = 0

def levelProg(xp = 0, width = 30):
    left = width * xp // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']', f' {percent: 0f}%', sep = '', end = '', flush = True ) 


def showStats(self):
    global tof, xpForLevel
    levelProg()
    print("Health: {}/{}".format(self.health, self.maxhealth))
    print("Power: {}".format(self.damageMulti))
         
        # with Bar(" |=========== Level {} ============|\n".format(self.level), fill='=', max=xpForLevel) as bar:
        #     for i in range(xpForLevel):
        #         # while tof == "true":
        #         print("xp")
        #         # os.system('cls')
        #         print("These are your statistics:")

        #         bar.next(randint(1, xpForLevel))
        #         sleep(1)
        #     if bar >= xpForLevel:
        #         bar.finish()
                   
        #         # if Bar == 'FINISHED':
        #         print("\n \nHealth: {}/{}".format(self.health, self.maxhealth))
        #         print("Power: {}".format(self.damageMulti))
        #             tof = "false"
                    
        #         increment = input("\nIncrement Bar?: ")
        #         if increment == "n":
                
        #         else:
        #             amount = randint(1, 100)
        #             amount = input("How Much?: ")
        #             amount = int(amount)
        #             incamount = amount 
        #             bar.next(incamount)
        #             pass
            
        
    

        


class Goblin:
    def __init__(self, level):
        self.name = "Goblin"
        if level == "1":
            self.health = 30.0
            self.damage = 0.75
        elif level == "2":
            self.health = 45.0
            self.damage = 1.0
        elif level == "3":
            self.health = 55.0
            self.damage = 1.5
        
class Troll:
    def __init__(self, level):
        self.name = "Troll"
        if level == "1":
            self.health = 45.0
            self.damage = 0.75
        elif level == "2":
            self.health = 55.0
            self.damage = 1.0
        elif level == "3":
            self.health = 70.0
            self.damage = 1.5

class Giant_Spider:
    def __init__(self, level):
        self.name = "Giant Spider"
        if level == "1":
            self.health = 25.0
            self.damage = 0.75
        elif level == "2":
            self.health = 40.0
            self.damage = 1.0
        elif level == "3":
            self.health = 50.0
            self.damage = 1.5

class Bugbear:
    def __init__(self, level):
        self.name = "BugBear"
        if level == "1":
            self.health = 35.0
            self.damage = 0.75
        elif level == "2":
            self.health = 50.0
            self.damage = 1.0
        elif level == "3":
            self.health = 60.0
            self.damage = 1.5            

class Boss:
    def __init__(self):
        self.name = "Skeleton Mage"
        self.health = 500.0
        self.damage = 2

# ENUMS

# room types
ROOM = 1
HALL = 2

# config rowdata array indicies
C_LVL = 0
C_COL = 1
C_ROW = 2
C_TYPE = 3
C_DESTN = 4
C_DESTS = 5
C_DESTE = 6
C_DESTW = 7
C_DESTUP = 8
C_DESTDOWN = 9
C_DESTPORTAL = 10
C_ISLIT = 11
C_VISITED = 12
C_DESCNDX = 13
C_ITEMLIST = 14

# field array indicies
F_TYPE = C_TYPE - 3
F_DESTN = C_DESTN - 3
F_DESTS = C_DESTS - 3
F_DESTE = C_DESTE - 3
F_DESTW = C_DESTW - 3
F_DESTUP = C_DESTUP - 3
F_DESTDOWN = C_DESTDOWN - 3
F_DESTPORTAL = C_DESTPORTAL - 3
F_ISLIT = C_ISLIT - 3
F_VISITED = C_VISITED - 3
F_DESCNDX = C_DESCNDX - 3
F_ITEMLIST = C_ITEMLIST - 3


lvlcnt = 4
rowcnt = -1
colcnt = -1
fldcnt = -1

# game_name = ""
# game_context = ""
# game_levels = ""
# game_version = ""
# game_fnameprefix = ""

class Game:
    name = "Generic"
    context = "Test"
    levels = "1"
    version = "0.0"
    fnameprefix = "./game-lvl-"

    def __init__(self):
        # verbosity = verbosity

        config = ConfigParser()
        config.read("./game.cfg")
        self.name = config.get("Realm", "Name")
        self.context = config.get("Realm", "Context")
        self.levels = config.get("Realm", "Levels")
        self.version = config.get("Realm", "Version")
        self.fnameprefix = config.get("Realm", "FNamePrefix")
        print("The name of the game is '{}'".format(self.name))
        print("Context: {}".format(self.context))
        print("Version: {}".format(self.version))
        print("Levels: {}".format(self.levels))
        print("file prefix: {}".format(self.fnameprefix))
        print()

game = Game()
player = Player()

levels = []

action_dict = {
    "attack":       "a",
    "block":        "b",
    "drop":         "d",
    "down":         "do",
    "east":         "e",
    "flee":         "f",
    "help":         "h",
    "inventory":    "i",
    "look":         "l",
    "north":        "n",
    "open":         "o",
    "quit":         "q",
    "south":        "s",
    "take":         "t",
    "use":          "u",
    "up":           "up",
    "west":         "w",
    "wield":        "wi",
    "stats":        "st",
    }

path_dict = { }

armor_items = [
    "Leather Helmet", "Leather Chestplate", "Leather Leggings", "Leather Boots", 
    "Chainmail Helmet", "Chainmail Chestplate", "Chainmail Leggings+", "Chainmail Boots+", 
    "Bronze Helmet", "Bronze Chestplate", "Bronze Leggings", "Bronze Boots", 
    "Iron Helmet", "Iron Chestplate", "Iron Leggings", "Iron Boots", 
    "Dragon Scale Helmet", "Dragon Scale Chestplate", "Dragon Scale Leggings", "Dragon Scale Boots"
    ]

weeapon_items = [
    "Rusty Butterknife",
    "Rusty Longsword",
    "Bronze Dagger",
    "Bronze Sword",
    "Iron Dagger",
    "Iron Sword",
    "Goblin Cleaver",
    "Dragon's Bane"
    ]

ring_items = [
    "Lucky Ring",
    "Invisibilty Ring",
    "Power Ring",
    "Defense Ring"
    ]

item_lists = [[],
              ["Leather Boots+", "Rusty Butterknife"],
              [],
              # ["Atomic Bomb", "ice-cream cone", "red dress", "Hammer of Thor"],
              [],
              [],
              ["Leather Chestpiece", "Leather Leggings+"],
              ["Leather Leggings+", "Power Ring"],
              ["Rusty Longsword", "Leather Helmet"],
              [],
              ["Power Ring", "Leather Boots+"]
             ]

hall_descs = [
    "|",
    "in a dimly lit corridor with ancient runes etched into the walls.|in the runes corridor.",
    "in a narrow hallway filled with the echoes of distant whispers.|in the echo hallway.",
    "in a claustrophobic hallway with flickering, ghostly lights.|in a claustrophobic hallway.",
    "in a corridor adorned with eerie portraits of long-forgotten rulers.|in the portraits corridor.",
    "in a damp, musty corridor with patches of luminescent moss.|in the moss corrridor.",
    "in a corridor that seems to whisper secrets to those who pass through.|in the whisper corridor.",
    "in an unsettling passageway lined with petrified statues of adventurers.|in the statues passageway.",
    "in a hallway where the walls seem to pulse and throb with a mysterious energy.|in the pulsing hallway.",
    "in a narrow passage filled with the bones of unfortunate explorers who came before.|in the bones passage.",
    "in a hall with strange, shifting symbols that seem to rearrange themselves.|in the symbols hall.",
    "in a passageway lined with grotesque carvings of monstrous creatures.|in the carvings passageway.",
    "in a hall where the walls seem to close in and shift as if alive.|in the shifty hall.",
    "in a corridor adorned with tattered banners of a long-forgotten kingdom.|in the banners corridor.",
    "in a dimly lit tunnel with strange, pulsating fungi growing along the walls.|in the fungi tunnel.",
    "in a claustrophobic tunnel filled with the sound of skittering creatures.|in a claustrophobic tunnel.",
    "in a corridor adorned with cryptic, indecipherable writings.|in the writings corridor.",
    "in a passageway that might lead to another dimension.|in the dimension passageway.",
    "in a damp, musty tunnel with the faint scent of decay lingering in the air.|in the decay tunnel.",
    "in a corridor where the shadows seem to dance and twist unnaturally.|in the shadows corridor.",
    "in a hall adorned with faded tapestries depicting forgotten battles.|in the battle-tapestries hall.",
    "in a passageway lined with the bones of ancient beasts long extinct.|in the bones passageway.",
    "in a hall where the air crackles with arcane energy, creating an eerie glow.|in the crackle hall.",
    "in a claustrophobic passage with the sound of distant, mournful wails.|in the wails passage.",
    "in a hall where the walls seem to writhe and twist like living flesh.|in the writhing-flesh hall.",
    "in a corridor adorned with the remnants of shattered, ornate mirrors.|in the mirror corridor.",
    "in a passageway filled with the eerie, ethereal glow of ghostly apparitions.|in the apparition passageway.",
    "in a passageway lined with the remnants of long-extinguished torches.|in the dead-torch passageway."
]

room_descs = [
    "|",
    "in a small room with a large button in the center of the floor that says \"Press Me\"; there is a tiny man trying desparately to get your attention.|in the button room.",
    "in a space that looks like a ransacked chicken coop, the chickens are all gone, the hungry wolves are still here.|in the chicken-wolf space.",
    "in a well-tended yard with a freshly dug empty grave, you find it unsettling that the gravestone has your name on it.|in the well-tended yard.",
    "in a dilapidated graveyard, the nearest tombstone reads, \"Owen Moore has gone away, owin' more than he could pay.\"|in the dilapidated graveyard.",
    "in an anti-gravity chamber; you are standing on the ceiling and experiencing a strong sense of virtigo.|in the anti-gravity chamber.",
    "on the holodeck of the Starship Enterprise, but you are just a CGI illusion.|on the holodeck.",
    "in a virtual room in an adventure game; don't you have anything better to do?|in the virtual room.",
    "in a dark vestibule; there is a note scrawled upon the wall that says, \"You'll be sorry.\"|in the dark vestibule.",
    "in a room where an annoying buzzing sound can be heard.|in the buzzing room.",
    "in a room with a blood-soaked altar in the middle.|in the altar room.",
    "in a room with a cold, hard floor.|in the cold-hard floor room",
    "in a strangely decorated room, and an even stranger state of mind.|in the strange room.",
    "in a cramped space with a low ceiling.|in a cramped space.",
    "in yet another room, but nobody really cares.|in yet another room.",
    "in a room, there is nothing of interest here.|in the boring room.",
    "in a sauna room, it is hot and humid in here.|in the sauna.",
    "in a damp chamber that crackles as you step across the floor; perhaps it is the crunch of dead (or living) insects.|in the crunch chamber.",
    "in a chamber with millions of cockroaches covering the walls and floor.|in the cockroach chamber.",
    "in a musty chamber, what is that smell?|in the musty chamber.",
    "in another room, were you expecting something else?|in another room.",
    "in a cozy chamber with hearts decorating the walls, some are still beating.|in the cozy chamber.",
    "in a dimly lit room with newly painted walls, intended to hide the copious blood stains.|in the fresh-paint room.",
    "in a room; you hear a loud snoring sound, but see nothing that could be the source.|in the snoring room.",
    "in a very clean stable, surrounded by brightly colored ponies with smiley faces on their foreheads; they appear to be angry that you are here.|in the clean stable.",
    "in a dimly lit chamber with an unsettlingly comfortable-looking sarcophagus in the center.|in the sarchophagus room.",
    "in a room filled with cobwebs and the faint sound of ghostly laughter echoing from the shadows.|in the cobweb room.",
    "in a disco venue with skeletons dancing to an eternal, unheard beat.|in the disco venue.",
    "in the target chamber of a huge cyclotron; you should avoid passing your modified DNA to offspring.|in the cyclotron.",
    "in a cramped space cluttered with broken furniture and a \"Beware of the Dragon\" sign that seems oddly out of place.|in a cramped space.",
    "in a chamber with a bubbling cauldron emitting colorful smoke and a sign reading \"Free potions, take at your own risk.\"|in the cauldron chamber",
    "in a room adorned with intricate murals depicting heroic stick figures battling fearsome stick-figure monsters.|in the mural room.",
    "in a damp cellar housing barrels of questionable liquids and a sign that says \"Drink at your own peril.\"|in the damp cellar.",
    "in an echoing chamber with mysterious whispers bouncing off the walls, arguing about who forgot to pay the dungeon rent.|in the echo chamber.",
    "in a cluttered library containing dusty tomes and scrolls with titles like \"101 Ways to Escape a Dungeon\" and \"Cooking with Slime: A Culinary Adventure.\"|in the library.",
    "in a room with a faulty torch, causing flickering shadows to create a shadow puppet show of heroic adventurers fighting imaginary monsters.|in the flickering torch room.",
    "in a space filled with mechanical contraptions of unknown purpose, emitting peculiar sounds that resemble catchy dungeon tunes.|in the mechanical room.",
    "in a dark room with a single, ominous pedestal in the center, holding a \"Do Not Touch\" button that's just begging to be pressed.|in the pedestal room.",
    "in a chamber with a series of riddles etched into the walls, each with the answer \"moldy cheese\" written in tiny letters underneath.|in the riddle chamber.",
    "in a room adorned with shimmering crystals that refract light in mesmerizing patterns, forming messages like \"Clean Me\" and \"Help, I'm stuck in a dungeon!\"|in the crystal room.",
    "in an abandoned workshop littered with half-finished inventions and a note that says \"I regret nothing...except, perhaps, the exploding potions.\"|in the abandoned workshop.",
    "in a chamber containing a collection of oddities and curios from distant lands, each with a label that says \"Totally not cursed... probably.\"|in the curios chamber.",
    "in a dimly lit space with a series of peculiar, glowing runes etched into the floor, spelling out \"This way to the treasure... or a very deadly monster.\"|in the glowing runes space.",
    "in a cramped space with a comically oversized chair and a tiny table, as if designed for a dungeon-dwelling giant with a sense of humor.|in the oversized chair space.",
    "in a chamber adorned with eerie, yet oddly charming, paintings of long-deceased nobility, all with exaggerated mustaches and monocles.|in the nobility chamber.",
    "in a room filled with ancient, cobweb-covered suits of armor, frozen in time, all striking heroic poses that are just a tad too dramatic.|in the ancient armor room.",
    "in a space with a glistening pool of water, its depths concealing mysterious secrets, such as the lost socks of many adventurers who came before.|in the pool space.",
    "in a cluttered chamber with piles of discarded trinkets and curiosities, tempting exploration and the occasional unexpected banana peel slip.|in the trinkets chamber.",
    "in a room with an inexplicably opening, seemingly leading to nowhere, where the sound of frustrated dungeon builders can be heard in the distance.|in the unknown opening room.",
    "in a room adorned with elaborate, if slightly faded, tapestries that once told grand tales, now rewritten with added dragons and unicorns by a bored dungeon artist.|in the tapestries room.",
    "in an echoing hall with a series of comically exaggerated, larger-than-life statues, all striking poses that scream, \"Look at me, I'm important!\"|in the echo hall.",
    "in a chamber containing a collection of oddities and curios from distant lands, each with a unique story to tell and a strong desire not to be touched.|in the untouchables room.",
    "in a dimly lit space with a series of peculiar, glowing runes etched into the floor, spelling out \"Beware of the grumpy dungeon troll, he hasn't had his coffee yet.\"|in the glowing runes space.",
    "in a room with an out-of-place, obnoxiously colorful rug that clashes with the surroundings, as if the decorator had a passion for bold, dungeon-chic fashion.|in the rug room.",
    "in a cavernous chamber with an unsettling, yet strangely mesmerizing, natural formation that looks suspiciously like a sleeping dragon.|in the cavernous chamber.",
    "in an overgrown room, where nature has reclaimed the space, creating an eerie, verdant underworld, complete with a sign that says \"Welcome to the Plant Kingdom, where every step is a potential slip 'n slide adventure!\"|in the nature room.",
    "in a cramped chamber housing an eccentric collection of mismatched furniture and decorations, as if a dungeon decorator had a yard sale and just couldn't resist a bargain.|in the furniture room.",
    "in a room with an elaborate, if slightly malfunctioning, mechanism that seems to serve no purpose, except to occasionally spray unsuspecting adventurers with water.|in the eloborate mechanism room.",
    "in a space adorned with peculiar, comically exaggerated portraits of historical figures, all with added mustaches and pirate hats.|in the portrait space.",
    "in a chamber with an inexplicably misplaced window, offering a view of an alien landscape, complete with a sign that says \"No admittance to the dungeon moon, please use your imagination responsibly.\"|in an alien landscape.",
    "in a new dimension not just of sight and sound, but of mind; unfortunately you recently lost your mind and can't remember where you left it.|in the Twilight Zone.",
    "in a dimly lit room with a series of peculiar, if slightly unnerving, taxidermy displays of mythical creatures, all wearing name tags that say \"Frank the Friendly Dragon\" and \"Barry the Bashful Basilisk.\"|in the taxidermy room.",
    "in a cluttered space filled with forgotten odds and ends, hinting at past inhabitants, including a diary that reads, \"Day 248: Still lost in this confusing dungeon. Send snacks.\"|in the odds-and-ends room."
]

fixed_descs = [
    "|",
    "in the Magic shop; there are several displays with potions, spells, and rings for sale.  The proprietor behind the counter is an old man.  He looks at you and says, \"I used to be an adventurer like you. Then I took an arrow in the knee.\"|in the Magic shop.",
    "in your quaint, but comfortable cottage.  There is a storage chest here.|in the comfortable cottage.",
    "at the village center.  You can see a Magic shop to the west, an Armory shop to the east, your house to the north, and a sinister-looking arch to the south. |at the village center. ",
    "at the dungeon entrance; you feel a dark-sense of foreboding as you consider going descending the stairs or running away like a scared rabbit.|at the dungeon entrance.",
    "in the Armory shop. Do not try to cheat this well-armed shopkeeper.|in the Armory shop.",
]

# def config_init():
#     global game_name
#     global game_context
#     global game_levels
#     global game_version
#     global game_fnameprefix

#     config = ConfigParser()
#     config.read("./game.cfg")
#     game_name = config.get("Realm", "Name")
#     game_context = config.get("Realm", "Context")
#     game_levels = config.get("Realm", "Levels")
#     game_version = config.get("Realm", "Version")
#     game_fnameprefix = config.get("Realm", "FNamePrefix")
#     print("The name of the game is '{}'".format(game_name))
#     print("Context: {}".format(game_context))
#     print("Version: {}".format(game_version))
#     print("Levels: {}".format(game_levels))
#     print("file prefix: {}".format(game_fnameprefix))
#     print()

def print_error(txt):
    # ESC = '\x1b'
    print('\x1b[41m' + txt + '\x1b[0m')
    # print(ESC + '[42m' + txt + ESC + '[0m')
    # print(ESC + '[43m' + txt + ESC + '[0m')
    # print(ESC + '[44m' + txt + ESC + '[0m')
    # print(ESC + '[45m' + txt + ESC + '[0m')
    # print(ESC + '[46m' + txt + ESC + '[0m')
    # print(ESC + '[47m' + txt + ESC + '[0m')
    # print()    
    # print(ESC + '[101m' + txt + ESC + '[0m')
    # print(ESC + '[102m' + txt + ESC + '[0m')
    # print(ESC + '[103m' + txt + ESC + '[0m')
    # print(ESC + '[104m' + txt + ESC + '[0m')
    # print(ESC + '[105m' + txt + ESC + '[0m')
    # print(ESC + '[106m' + txt + ESC + '[0m')
    # print(ESC + '[107m' + txt + ESC + '[0m')

def print_warning(txt):
    # ESC = '\x1b'
    print('\x1b[44m' + txt + '\x1b[0m')

##### Title Screen #####
def title_screen_selections():
    while True:
        option = input(">> ").lower()
        if "play".startswith(option):
            print()
            main()
            return
        elif "help".startswith(option):
            help_menu()
            return
        elif "quit".startswith(option):
            sys.exit()
            return
        print("Invalid choice. Please try again. (""Play"", ""Help"", ""Quit"")")
            
def title_screen():     
    os.system('cls')
    print("##############################")
    print("######## Dark Descent ########")
    print("##############################")
    print("           -Play-            ")
    print("           -Help-            ")
    print("           -Quit-            ")
    print("Copyright © 2024 JB Productions")
    print("")
    title_screen_selections()

def help_menu():
    os.system('cls')
    print("Insert help text here.")
    print("Press ENTER to return to main menu.")
    option = input(" ").lower
    if (" ").startswith(option):
        title_screen()
             
    else:
        title_screen()

def analyze_level(lvlnum):
    global rowcnt
    global colcnt
    global fldcnt

    linecnt = 0
    maxrows = 0
    maxcols = 0
    valuecnt = 0
    rslt = (0, 0, 0)

    with open("{}{:0>3d}.csv".format(game.fnameprefix,lvlnum), 'r') as lvl:
        line = lvl.readline().strip()   # skip header row
        while line:
            line = lvl.readline().strip()
            if line == '':
                break
            linecnt += 1

            if verbosity > 5:
                print("line ({}): '{}'".format(linecnt, line))
            rowdata = line.split(',')
            if valuecnt > 0 and len(rowdata) != valuecnt:
                print("line {} has unexpected number of values, value count: {}, expected {}".format(linecnt, len(rowdata), valuecnt))
            else:
                valuecnt = len(rowdata)

            spcLvl = int(rowdata[C_LVL])
            spcCol = int(rowdata[C_COL])
            spcRow = int(rowdata[C_ROW])
            spcType = int(rowdata[C_TYPE])
            spcDestN = int(rowdata[C_DESTN])
            spcDestS = int(rowdata[C_DESTS])
            spcDestE = int(rowdata[C_DESTE])
            spcDestW = int(rowdata[C_DESTW])
            spcDestUp = int(rowdata[C_DESTUP])
            spcDestDown = int(rowdata[C_DESTDOWN])
            spcDestPortal = int(rowdata[C_DESTPORTAL])
            spcDestLit = int(rowdata[C_ISLIT])
            spcVisited = int(rowdata[C_VISITED])
            spcDesc = random.randint(0,len(room_descs)-1)
            spcItemList = int(rowdata[C_ITEMLIST])

            rows = spcRow + 1
            if rows > maxrows:
                maxrows = rows
                
            cols = spcCol + 1
            if cols > maxcols:
                maxcols = cols
    
    rowcnt = maxrows
    colcnt = maxcols
    fldcnt = valuecnt - 3   # -3: lvl,col,row values are not included in field cnt
    rslt = (colcnt, rowcnt, fldcnt)
    if verbosity > 5:
        print("analyze: row cnt: {}, col cnt: {}, fld cnt: {}".format(rowcnt, colcnt, fldcnt))

    return rslt

def get_dest_prompt(lvl, col, row):
    # global spcs

    prompt = ""
    
    # itemlist_ndx = spcs[lvl, col, row, F_ITEMLIST]
    # if itemlist_ndx > 0:
    #     for item in item_lists[itemlist_ndx]:
    #         if item[0] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
    #             article = "an"
    #         else:
    #             article = "a"
                    
    #         print("There is {} {}.".format(article, item))
        
    door_list = []
    if levels[lvl][col, row, F_DESTN] > -1:
        door_list.append("north")
    if levels[lvl][col,row,F_DESTS] > -1:
        door_list.append("south")
    if levels[lvl][col,row,F_DESTE] > -1:
        door_list.append("east")
    if levels[lvl][col,row,F_DESTW] > -1:
        door_list.append("west")

    stair_list = []
    if levels[lvl][col, row, F_DESTUP] > -1:
        stair_list.append("up")
    if levels[lvl][col,row,F_DESTDOWN] > -1:
        stair_list.append("down")

    portal_list = []
    if levels[lvl][col, row, F_DESTPORTAL] > -1:
        portal_list.append("portal")
        
    enemy_list = []
    if levels[lvl][col, row, F_DESTPORTAL] > -1:
        enemy = randint
        portal_list.append("portal")

    for dir in door_list:
        prompt += "\nThere is a door to the {}.".format(dir)
    for dir in stair_list:
        prompt += "\nThere are stairs leading {}.".format(dir)
    for dir in portal_list:
        prompt += "\nThere is a {} in the room.".format(dir)
    for dir in enemy_list:
        pass

    return prompt

def get_items(lvl, col, row):
    prompt = ""
    
    itemlist_ndx = levels[lvl][col, row, F_ITEMLIST]
    if itemlist_ndx > 0:
        for item in item_lists[itemlist_ndx]:
            if item[len(item)-1] == "+":
                verb_clause = "are"
                item = item[0:len(item)-1]
            else:
                if item[0].lower() in ["a", "e", "h", "i", "o", "u"]:
                    verb_clause = "is an"
                else:
                    verb_clause = "is a"
                    
            prompt += "\nThere {} {} here.".format(verb_clause, item)
    
    return prompt
    

def get_level(lvlnum):
    linecnt = 0
    fname = "{}{:0>3d}.csv".format(game.fnameprefix,lvlnum)
    if verbosity > 25: print("opening level {}: '{}'".format(lvlnum,fname))
    with open(fname, 'r') as lvl:
        if verbosity > 25: print("{} open".format(fname))
        line = lvl.readline().strip()
        while line:
            line = lvl.readline().strip()
            if line == '':
                break

            linecnt += 1

            if verbosity > 25:
                print("line ({}): '{}'".format(linecnt, line))
                
            rowdata = line.split(',')

            spcLvl = int(rowdata[C_LVL])
            spcCol = int(rowdata[C_COL])
            spcRow = int(rowdata[C_ROW])
            spcType = int(rowdata[C_TYPE])
            spcDestN = int(rowdata[C_DESTN])
            spcDestS = int(rowdata[C_DESTS])
            spcDestE = int(rowdata[C_DESTE])
            spcDestW = int(rowdata[C_DESTW])
            spcDestUp = int(rowdata[C_DESTUP])
            spcDestDown = int(rowdata[C_DESTDOWN])
            spcDestPortal = int(rowdata[C_DESTPORTAL])
            spcDestLit = int(rowdata[C_ISLIT])
            spcVisited = int(rowdata[C_VISITED])
            if int(rowdata[C_DESCNDX]) > -1:
                if spcType == 2:
                    spcDesc = random.randint(0,len(hall_descs)-1)
                else:
                    spcDesc = random.randint(0,len(room_descs)-1)
            else:
                spcDesc = rowdata[C_DESCNDX]
            spcItemList = int(rowdata[C_ITEMLIST])

            levels[spcLvl][spcCol, spcRow, F_TYPE] = spcType
            levels[spcLvl][spcCol, spcRow, F_DESTN] = spcDestN
            levels[spcLvl][spcCol, spcRow, F_DESTS] = spcDestS
            levels[spcLvl][spcCol, spcRow, F_DESTE] = spcDestE
            levels[spcLvl][spcCol, spcRow, F_DESTW] = spcDestW
            levels[spcLvl][spcCol, spcRow, F_DESTUP] = spcDestUp
            levels[spcLvl][spcCol, spcRow, F_DESTDOWN] = spcDestDown
            levels[spcLvl][spcCol, spcRow, F_DESTPORTAL] = spcDestPortal
            levels[spcLvl][spcCol, spcRow, F_ISLIT] = spcDestLit
            levels[spcLvl][spcCol, spcRow, F_VISITED] = spcVisited
            levels[spcLvl][spcCol, spcRow, F_DESCNDX] = spcDesc
            levels[spcLvl][spcCol, spcRow, F_ITEMLIST] = spcItemList


def destination(lvl, col, row, dir):
    ndir = 0
    if dir == 'n':
        os.system('cls')
        ndir = F_DESTN
    elif dir == 's':
        ndir = F_DESTS
    elif dir == 'e':
        ndir = F_DESTE
    elif dir == 'w':
        ndir = F_DESTW
    elif dir == 'up':
        ndir = F_DESTUP
    elif dir == 'do':
        ndir = F_DESTDOWN
    else:
        return -1

    return levels[lvl][col, row, ndir]


def get_lvl(dest):
    dest -= int(dest % 1000000)
    return int(dest / 1000000)

def get_col(dest):
    dest = int(dest % 1000000)
    dest -= int(dest % 1000)
    return int(dest / 1000)

def get_row(dest):
    return int(dest % 1000)

def get_dest_key(lvl, col, row):
    # return "{}".format(lvl*1000000 + col*1000 + row)
    return lvl*1000000 + col*1000 + row

def location_txt (lvl, col, row):
    if levels[lvl][col,row,F_TYPE] == 1:
        spctype = "room"
    elif levels[lvl][col,row,F_TYPE] == 2:
        spctype = "hall"
    else:
        spctype = "unk?"

    return "<{} ({},{},{})>".format(spctype, lvl, col, row)

def look_room(lvl, col, row, full):
    spcType = levels[lvl][col,row,F_TYPE]
    if levels[lvl][col,row,F_DESCNDX] < 0:
        if full:
            levels[lvl][col,row,F_VISITED] = 0
        visited = levels[lvl][col,row,F_VISITED]
        desc0 = fixed_descs[-levels[lvl][col,row,F_DESCNDX]]
        if visited:
            desc = desc0.split("|")[1]
        else:
            desc = desc0.split("|")[0]
            levels[lvl][col,row,F_VISITED] = 1
    else:
        if spcType == 1:
            if full:
                levels[lvl][col,row,F_VISITED] = 0
            visited = levels[lvl][col,row,F_VISITED]
            desc0 = room_descs[levels[lvl][col,row,F_DESCNDX]]
            if visited:
                desc = desc0.split("|")[1]
            else:
                desc = desc0.split("|")[0]
                levels[lvl][col,row,F_VISITED] = 1
        else:
            if full:
                hall_descs[levels[lvl][col,row,F_VISITED]] = 0
            visited = levels[lvl][col,row,F_VISITED]
            desc0 = hall_descs[levels[lvl][col,row,F_DESCNDX]]
            if visited:
                desc = desc0.split("|")[1]
            else:
                desc = desc0.split("|")[0]
                levels[lvl][col,row,F_VISITED] = 1
                
        if desc == "":
            if spcType == 1:
                desc = "a room."
            else:
                desc = "a hallway."
        
    print("{}\nYou are {}".format(location_txt(lvl, col, row), desc))
    if desc[len(desc)-1] != " ":
        prompt = get_dest_prompt(lvl, col, row)
        if prompt > "":
            print(prompt)
    prompt = get_items(lvl, col, row)
    if prompt > "":
        print(prompt)
        
def get_action(prompt):
    action_cmd = input(prompt).lower()
    for key in action_dict.keys():
        if key.startswith(action_cmd):
            action = action_dict[key]
            return action
    return ""
    
def test_movement():
    lvl = 0
    col = 1
    row = 1
    full = False
    while True:
        look_room(lvl, col, row, full)
        full = False
        action = get_action(">>> ")
        if action == "q":
            os.system('cls')
            title_screen()
            continue
        if action == "l":
            os.system('cls')
            print
            full = True
            continue
        if action == "u":
            os.system('cls')
            print_warning("Nothing to use.")
            continue
        if action == "d":
            os.system('cls')
            print_warning("Nothing to drop.")
            continue
        # if action == "st":
        #     os.system('cls')
        #     print("These are your statistics:")
        #     with Bar(" |=========== Level {} ============|\n".format(playerLvl), fill='=', max=xpForLevel) as bar:
        #         while lvlInc == 0:
        #             for i in range(xpForLevel):
        #                 bar.next(randint(1, xpForLevel))
        #                 time.sleep(1)

            # showStats(self)
            continue
        if not action in ['n','s','e','w','up','do']:
            os.system('cls')
            print_error("Invalid command, try again")
            continue
        dest = destination(lvl, col, row, action)
        if dest < 0:
            print_warning("You cannot move in that direction")
            continue
        lvl = get_lvl(dest)
        col = get_col(dest)
        row = get_row(dest)
        print("lvl->{}, col->{}, row->{}".format(lvl, col, row))
        os.system('cls')
        

def check_path_dict(dest):
    global path_dict

    if dest > -1:
        if dest in path_dict:
            path_dict[dest] += 1
        else:
            path_dict[dest] = 1
    
def update_paths():    
    for lvl in range(len(levels)):
        spcs = levels[lvl]
        shape = np.shape(spcs)
        cols = shape[0]
        rows = shape[1]
        for col in range(cols):
            for row in range(rows):
                dest = levels[lvl][col, row, F_DESTN]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTS]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTE]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTW]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTUP]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTDOWN]
                check_path_dict(dest)
                dest = levels[lvl][col, row, F_DESTPORTAL]
                check_path_dict(dest)
    
    print("{}".format(path_dict.keys()))
    
def check_paths():    
    for lvl in range(len(levels)):
        spcs = levels[lvl]
        shape = np.shape(spcs)
        cols = shape[0]
        rows = shape[1]
        for col in range(cols):
            for row in range(rows):
                key = get_dest_key(lvl, col, row)
                if not key in path_dict:
                    print("[{},{},{}] :  {} not in path dictionary".format(lvl, col, row, key))
    
    
    
def print_map(lvl):
    shape = np.shape(levels[lvl])
    cols = shape[0]
    rows = shape[1]
    # flds = shape[2]
    desc = ["", ""]
    for row in range(rows):
        separatortxt = "+"
        toptxt = "|"
        desctxt0 = "|"
        desctxt1 = "|"
        lvltxt = "|"
        coltxt = "|"
        rowtxt = "|"
        bottxt = "|"
        
        # "{}{:0>3d}.csv".format(game.fnameprefix,levelcnt)
        
        for col in range(cols):
            active = get_dest_key(lvl, col, row) in path_dict

            spcType = levels[lvl][col,row,F_TYPE]
            if not active:
                if spcType == 1:
                    desc1 = "unused room"
                else:
                    desc1 = "unused hallway"
            else:
                if levels[lvl][col,row,F_DESCNDX] < 0:
                    desc0 = fixed_descs[-levels[lvl][col,row,F_DESCNDX]]
                    desc1 = desc0.split("|")[1].replace(".", "").replace("-", " ").rstrip()
                else:
                    if spcType == 1:
                        desc0 = room_descs[levels[lvl][col,row,F_DESCNDX]]
                        desc1 = desc0.split("|")[1].replace(".", "").replace("-", " ").rstrip()
                    else:
                        desc0 = hall_descs[levels[lvl][col,row,F_DESCNDX]]
                        desc1 = desc0.split("|")[1].replace(".", "").replace("-", " ").rstrip()
                            
                    if desc1 == "":
                        if spcType == 1:
                            desc1 = "unknown room"
                        else:
                            desc1 = "unknown hallway"

            desc2 = desc1.split(" ")
            if len(desc2) < 2:
                desc[0] = desc2
                desc[1] = ""
            else:
                desc[0] = desc2[len(desc2)-2]
                if len(desc[0]) > 7:
                    desc[0] = desc[0][0:7]
                desc[1] = desc2[len(desc2)-1]
                if len(desc[1]) > 7:
                    desc[1] = desc[1][0:7]
            # print("'{}'  -->  '{}' - '{}'".format(desc1, desc[0], desc[1]))

            separatortxt += "-------+"
            
            itemlist_ndx = levels[lvl][col, row, F_ITEMLIST]
            if itemlist_ndx > 0:
                itemcnt = len(item_lists[itemlist_ndx])
            else:
                itemcnt = 0
            
            if levels[lvl][col, row, F_DESTN] > -1:
                ndoor = "^"
            else:
                ndoor = " "

            if levels[lvl][col, row, F_DESTUP] > -1:
                upstairs = "/"
            else:
                upstairs = " "
                
            if levels[lvl][col, row, F_ISLIT]:
                islit = "*"
            else:
                islit = " "

            toptxt += "{:2d} {}{} {}|".format(itemcnt, ndoor, upstairs, islit)
            

            if levels[lvl][col, row, F_DESTUP] > -1:
                upstairs = "/"
            else:
                upstairs = " "
            if levels[lvl][col,row,F_DESTDOWN] > -1:
                downstairs = "\\"
            else:
                downstairs = " "
            portal_list = []
            if levels[lvl][col, row, F_DESTPORTAL] > -1:
                portal_list.append("portal")
            
            # levels[lvl][col,row,F_DESTN],
            # levels[lvl][col,row,F_DESTS],
            # levels[lvl][col,row,F_DESTE],
            # levels[lvl][col,row,F_DESTW],
            # levels[lvl][col,row,F_DESTUP],
            # levels[lvl][col,row,F_DESTDOWN],
            # levels[lvl][col,row,F_DESTPORTAL],
            # levels[lvl][col,row,F_ISLIT],

            
            desctxt0 += "{:7s}|".format(desc[0])
            desctxt1 += "{:7s}|".format(desc[1])
            
            if levels[lvl][col,row,F_DESTS] > -1:
                sdoor = "v"
            else:
                sdoor = " "
            if levels[lvl][col,row,F_DESTE] > -1:
                edoor = ">"
            else:
                edoor = " "
            if levels[lvl][col,row,F_DESTW] > -1:
                wdoor = "<"
            else:
                wdoor = " "
        
            lvltxt += "  {:0>3d}  |".format(lvl)
            coltxt += "{} {:0>3d} {}|".format(wdoor, col, edoor)
            rowtxt += "  {:0>3d}  |".format(row)

            if levels[lvl][col, row, F_DESTPORTAL] > -1:
                portal = "@"
            else:
                portal = " "
            
            if levels[lvl][col, row, F_TYPE] == 1:
                spctype = "R"
            else:
                spctype = "H"
            
            bottxt += "  {}{}{} {}|".format(portal, sdoor, downstairs, spctype)
            
        print(separatortxt)
        print(toptxt)
        print(desctxt0)
        print(desctxt1)
        print(lvltxt)
        print(coltxt)
        print(rowtxt)
        print(bottxt)

    print(separatortxt)

##### Easter Egg 1 #####
def egg1():
    

def main():
    # config_init()

    levelcnt = 0
    while os.path.isfile("{}{:0>3d}.csv".format(game.fnameprefix,levelcnt)):
        rslt = analyze_level(levelcnt)
        cols = rslt[0]
        rows = rslt[1]
        flds = rslt[2]
        
        spcs = np.arange(cols * rows * flds).reshape((cols,rows,flds))
        levels.append(spcs)
        if verbosity > 5:
            print("level {} array elements: {}, arranged as {} cols x {} rows x {} flds".format(levelcnt, np.size(spcs), cols, rows, flds))
        print()
        levelcnt += 1
        
    print("{} levels found".format(levelcnt))
    for lvlnum in range(levelcnt):
        spcs = levels[lvlnum]
        if verbosity > 5:
            shape = np.shape(spcs)
            if verbosity > 25: print("spcs.shape: {}".format(shape))
            print("level {} array: {} elements, arranged as {} cols x {} rows x {} flds".format(lvlnum, np.size(spcs), shape[0], shape[1], shape[2]))
    print()

    for lvlnum in range(levelcnt):
        get_level(lvlnum)
        
    # sys.exit()

    if verbosity > 5:
        for lvl in range(levelcnt):
            shape = np.shape(levels[lvl])
            # if verbosity > 25: print("spcs.shape: {}".format(shape))
            for col in range(shape[0]):
                for row in range(shape[1]):
                    print("l:{} c:{} r:{} = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(lvl, col, row, 
                                                                                                    levels[lvl][col,row,F_TYPE],
                                                                                                    levels[lvl][col,row,F_DESTN],
                                                                                                    levels[lvl][col,row,F_DESTS],
                                                                                                    levels[lvl][col,row,F_DESTE],
                                                                                                    levels[lvl][col,row,F_DESTW],
                                                                                                    levels[lvl][col,row,F_DESTUP],
                                                                                                    levels[lvl][col,row,F_DESTDOWN],
                                                                                                    levels[lvl][col,row,F_DESTPORTAL],
                                                                                                    levels[lvl][col,row,F_ISLIT],
                                                                                                    levels[lvl][col,row,F_VISITED],
                                                                                                    levels[lvl][col,row,F_DESCNDX],
                                                                                                    levels[lvl][col,row,F_ITEMLIST]
                                                                                                    ))
    
    if False:
        print("len(room_descs): {},  len(hall_descs): {}".format(len(room_descs), len(hall_descs)))
    

        update_paths()
        check_paths()
            
        print_map(0)
        print()
        print_map(1)
        print()
        print_map(2)
        print()
        print_map(3)
    
        sys.exit()
    os.system('cls')
    test_movement()
    

if __name__ == '__main__':
    title_screen()

    # print()
    # main()


    if verbosity > 5:
        print("Done.")
