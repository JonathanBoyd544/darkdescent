import random
import sys
from collections import Counter

random.seed(None)

playHealt = 100.0
armVal = 0.0
damPlayAtt = 0.0
damEnemAtt = 0.0
enemHealth = 0.0
enemDamMulti = 0.0
level = 0
enemVal = "not defined"
lastTurn = "not defined"
mockInvSp = {}
mockInvWp = {}
mockInvAr = {}
mockInvOt = {}
mockEquip = {}

def setLvl():
    global level
    level = input("Define Level(1-3): ")
    if level == "1":
        level = 1
    elif level == "2":
        level = 2
    elif level == "3":
        level = 3
    else:
        print("invalid level selected, aborting ...")
        return
    print("Level: {}".format(level))
    setWeapon()

def setWeapon():
    global mockInvWp
    another = "y"
    while another == "y":
        weapon = input("Define Weapon\n1) Rusty Butterknife(0.5x)\n2) Rusty Longsword(1.0x)\n3) Bronze Dagger(1.2x)\n4) Bronze Sword(1.5x\n5) Iron Dagger(1.8x)\n6) Iron Sword(2.0x)\n7) Goblin Cleaver(2.5x\n8) Dragon's Bane(3.0x)\n>>>  ").lower()
        if weapon == '1':
            weapon = "Rusty Butterknife(0.5x)"
        elif weapon == '2':
            weapon = "Rusty Longsword(1.0x)"
        elif weapon == "3":
            weapon = "Bronze Dagger(1.2x)"
        elif weapon == "4":
            weapon = "Bronze Sword(1.5x)"
        elif weapon == "5":
            weapon = "Iron Dagger(1.8x)"
        elif weapon == "6":
            weapon = "Iron Sword(2.0x)"
        elif weapon == "7":
            weapon = "Goblin Cleaver (Great Axe)(2.5x)"
        elif weapon == "8":
            weapon = "Dragon's Bane (Great Sword)(3.0x)"
        mockInvWp[weapon] = mockInvWp.get(weapon , 0) + 1
        print(" ")
        print("Weapons In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvWp.items()))
        print(" ")
        another = input("Add another weapon? (y/n): ").lower()
        print(" ")
        if another == "n":
            setArmor()

def setArmor():
    global mockInvAr
    another = "y"
    while another == "y":
        helmet = input("Enter chosen helmet\n1) leather(+1)\n2) chainmail(+2)\n3) bronze(+4\n4) iron(+7)\n5) dragon scale(+13)\n>>> ").lower()
        if helmet == "1":
            helmet = "Leather Helmet(1pt)"
        elif helmet == "2":
            helmet = "Chainmail Helmet(2pts)"
        elif helmet == "3":
            helmet = "Bronze Helmet(4pts)"
        elif helmet == "4":
            helmet = "Iron Helmet(7pts)"
        elif helmet == "5":
            helmet = "Dragon's Scale Helmet(13pts)"
        else:
            helmet = "<unkown>"
        mockInvAr[helmet] = mockInvAr.get(helmet , 0) + 1
        print(" ")
        print("Helmets In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvAr.items()))
        print(" ")

        chestplate = input("Enter chosen chestplate\n1) leather(+1)\n2) chainmail(+2)\n3) bronze(+4\n4) iron(+7)\n5) dragon scale(+13)\n>>> ").lower()
        if chestplate == "1":
            chestplate = "Leather Chestplate(3pts)"
        elif chestplate == "2":
            chestplate = "Chainmail Chestplate(5pts)"
        elif chestplate == "3":
            chestplate = "Bronze Chestplate(7pts)"
        elif chestplate == "4":
            chestplate = "Iron Chestplate(12pts)"
        elif chestplate == "5":
            chestplate = "Dragon's Scale Chestplate(18pts)"
        else:
            chestplate = "<unkown>"
        mockInvAr[chestplate] = mockInvAr.get(chestplate , 0) + 1
        print(" ")
        print("Chestplates In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvAr.items()))
        print(" ")

        leggings = input("Enter chosen leggings\n1) leather(+1)\n2) chainmail(+2)\n3) bronze(+4\n4) iron(+7)\n5) dragon scale(+13)\n>>> ").lower()
        if leggings == "1":
            leggings = "Leather Leggings(2pts)"
        elif leggings == "2":
            leggings = "Chainmail Leggings(3pts)"
        elif leggings == "3":
            leggings = "Bronze Leggings(5pts)"
        elif leggings == "4":
            leggings = "Iron Leggings(10pts)"
        elif leggings == "5":
            leggings = "Dragon's Scale Leggings(16pts)"
        else:
            leggings = "<unkown>"
        mockInvAr[leggings] = mockInvAr.get(leggings , 0) + 1
        print(" ")
        print("Leggings In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvAr.items()))
        print(" ")

        boots = input("Enter chosen boots\n1) leather(+1)\n2) chainmail(+2)\n3) bronze(+4\n4) iron(+7)\n5) dragon scale(+13)\n>>> ").lower()
        if boots == "1":
            boots = "Leather Boots(1pt)"
        elif boots == "2":
            boots = "Chainmail Boots(2pts)"
        elif boots == "3":
            boots = "Bronze Boots(4pts)"
        elif boots == "4":
            boots = "Iron Boots(7pts)"
        elif boots == "5":
            boots = "Dragon's Scale Boots(13pts)"
        else:
            boots = "<unkown>"
        mockInvAr[boots] = mockInvAr.get(boots , 0) + 1
        print(" ")
        print("Boots In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvAr.items()))
        print(" ")
        another = input("Add more armor? (y/n): \n ").lower()
        print(" ")
        if another == "n":
            setSpells()
    
def setSpells():
    global mockInvSp, spellVal, spell, spellNum
    another = "y"
    while another == "y":
        spell = input("Select spell\n1) Fireball\n2) Lightning\n3) Wrath of Nature\n>>> ")
        if spell == "1":
            tier = input("Select fireball spell tier\n1) Tier 1(15dp)\n2) Tier 2(25dp)\n3) Tier 3(35dp)")
            if tier == "1":
                spell = "Fireball Spell[Tier 1](15dp)"
            elif tier == "2":
                spell = "Fireball Spell[Tier 2](25dp)"
            elif tier == "3":
                spell = "Fireball Spell[Tier 3](35dp)"
        if spell == "2":
            tier = input("Select lighning spell tier\n1) Tier 1(15dp)\n2) Tier 2(25dp)\n3) Tier 3(35dp)")
            if tier == "1":
                spell = "Lighning Spell[Tier 1](15dp)"
            elif tier == "2":
                spell = "Lightning Spell[Tier 2](25dp)"
            elif tier == "3":
                spell = "Lighning Spell[Tier 3](35dp)"
        if spell == "3":
            tier = input("Select wrath of nature spell tier\n1) Tier 1(15dp)\n2) Tier 2(25dp)\n3) Tier 3(35dp)")
            if tier == "1":
                spell = "Wrath of Nature Spell[Tier 1](15dp)"
            elif tier == "2":
                spell = "Wrath of Nature Spell[Tier 2](25dp)"
            elif tier == "3":
                spell = "Wrath of Nature Spell[Tier 3](35dp)"
        mockInvSp[spell] = mockInvSp.get(spell , 0) + 1
        print(" ")
        print("Spells In Inventory:")
        print('\n'.join("{}: {}".format(k, v) for k, v in mockInvSp.items()))
        another = input("Add another spell? (y/n): \n ").lower()
        print(" ")
        if another == "n":
            selEnem()
    
def selEnem():
    global enemHealth, enemDamMulti, enemVal, spellNum
    enemy = input("Define Enemy(goblin, troll, giant spider, bugbear, boss): ").lower()
    if "goblin".startswith(enemy):
        enemVal = "Goblin"
        if level == 1:
            enemHealth = 30.0
            enemDamMulti = 0.75
        elif level == 2:
            enemHealth = 45.0
            enemDamMulti = 1.0
        elif level == 3:
            enemHealth = 55.0
            enemDamMulti = 1.5
            
    elif "troll".startswith(enemy):
        enemVal = "Troll"
        if level == 1:
            enemHealth = 45.0
            enemDamMulti = 0.75
        elif level == 2:
            enemHealth = 55.0
            enemDamMulti = 1.0
        elif level == 3:
            enemHealth = 70.0
            enemDamMulti = 1.5

    elif "giant spider".startswith(enemy):
        enemVal = "Giant Spider"
        if level == 1:
            enemHealth = 25.0
            enemDamMulti = 0.75
        elif level == 2:
            enemHealth = 40.0
            enemDamMulti = 1.0
        elif level == 3:
            enemHealth = 50.0
            enemDamMulti = 1.5

    elif "bugbear".startswith(enemy):
        enemVal = "BugBear"
        if level == 1:
            enemHealth = 35.0
            enemDamMulti = 0.75
        elif level == 2:
            enemHealth = 50.0
            enemDamMulti = 1.0
        elif level == 3:
            enemHealth = 60.0
            enemDamMulti = 1.5

    elif "boss".startswith(enemy):
        enemVal = "Skeleton Mage"
        if level == 1:
            enemHealth = 200.0
            enemDamMulti = 2.0
        elif level == 2:
            enemHealth = 200.0
            enemDamMulti = 2.0
        elif level == 3:
            enemHealth = 200.0
            enemDamMulti = 2.0
    print("Enemy: {}, enemey health: {}, enemy damage multiplier: {}".format(enemVal, enemHealth, enemDamMulti))
#     first_turn()

# def first_turn():
#     global level
#     r3 = random.randint(1, 2)
#     if r3 == 1:
#         print("It is your turn. Attack or flee?")
#         decision = input(">>> ").lower()
#         if "attack".startswith(decision):
#             player_attack()
#         elif "flee".startswith(decision):
#             sys.exit()

#     elif r3 == 2:
#         enemy_attack()
#     main_combat()

# def player_attack():
#     global level, damageMulti, enemVal, enemHealth, lastTurn
#     if level == 1:
#         r1 = random.randint(1, 20)
#         damPlayAtt = r1 * damageMulti
#         enemHealth = enemHealth-damPlayAtt
#         # print("You deal %s damage to the %s. The %s has %s hp left" % (damPlayAtt, enemVal, enemVal, enemHealth))
#         print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
#         lastTurn = "player"
#     elif level == 2:
#         r1 = random.randint(5, 15)
#         damPlayAtt = r1 * damageMulti
#         enemHealth = enemHealth-damPlayAtt
#         print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
#         lastTurn = "player"
#     elif level == 3:
#         r1 = random.randint(5, 15)
#         damPlayAtt = r1 * damageMulti
#         enemHealth = enemHealth-damPlayAtt
#         print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
#         lastTurn = "player"
#     if enemHealth <= 0:
#         PlayerWin()
#     if playHealt <= 0:
#         PlayerDead()

# def enemy_attack():
#     global level, enemVal, enemHealth, enemDamMulti, playHealt, lastTurn
#     if level == 1:
#         r2 = random.randint(1, 10)
#         damEnemAtt = r2 * enemDamMulti * armVal
#         damEffect = damEnemAtt * armVal
#         playHealt = playHealt - damEffect
#         print(" ")
#         # print("The %s attacks, dealing %s damage (reduced by armor to %s). You have %s hp left." % (enemVal, damEnemAtt, damEffect, playHealt))
#         print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
#         print(" ")
#         lastTurn = "enemy"
#     elif level == 2:
#         r2 = random.randint(5, 15)
#         damEnemAtt = r2 * enemDamMulti * armVal
#         damEffect = damEnemAtt * armVal
#         playHealt = playHealt - damEffect
#         print(" ")
#         print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
#         print(" ")
#         lastTurn = "enemy"
#     elif level == 3:
#         r2 = random.randint(5, 15)
#         damEnemAtt = r2 * enemDamMulti * armVal
#         damEffect = damEnemAtt * armVal
#         playHealt = playHealt - damEffect
#         print(" ")
#         print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
#         print(" ")
#         lastTurn = "enemy"
#     if enemHealth <= 0.0:
#         PlayerWin()
#     if playHealt <= 0.0:
#         PlayerDead()

# def main_combat():
#     if lastTurn == "enemy":
#         print("It is your turn\n1) Attack\n2)Use Spell\n3) Swap Equipment\n4) Flee\n")
#         decision = input(">>> ").lower()
#         if decision == "1":
#             player_attack()
#         elif decision == "2":
#             useSpell()
#         elif decision == "3":
#             swapEquip()
#         elif decision == "4"
#             sys.exit()
#     elif lastTurn == "player":
#         enemy_attack()

# def useSpell():

# def swapEquip():

# def PlayerWin():
#     print("You have defeated the " + enemVal + "!\nPlay again or quit?")
#     option = input(">>> ").lower()
#     if "play again".startswith(option):
#         set_values()
#     else:
#         sys.exit()

# def PlayerDead():
#     print("You have been defeated by the " + enemVal + "!\nPlay again or quit?")
#     option = input(">>> ").lower()
#     if "play again".startswith(option):
#         set_values()
#     else:
#         sys.exit()




setLvl()
