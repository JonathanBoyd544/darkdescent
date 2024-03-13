import random
# from random import randint
import sys
random.seed(None)

level = 0
damageMulti = 0
secDamageMulti = 0
armVal = 0.0
damPlayAtt = 0.0
damEnemAtt = 0.0
enemHealth = 0.0
enemDamMulti = 0.0
playHealt = 100.0
enemVal = "not defined"
lastTurn = "not 1defined"
mockInv = []



def set_values():
    global level, damageMulti, enemHealth, enemDamMulti, enemVal, armVal
    
    armor = 0
    
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
    
    weapon = input("Define Weapon(Rusty Longsword, Bronze Sword, Dragon's Bane): ").lower()
    if "rusty butterknife".startswith(weapon):
        weapon = "Rusty Butterknife"
        damageMulti = 0.5
    elif "rusty longsword".startswith(weapon):
        weapon = "Rusty Longsword"
        damageMulti = 1.0
    elif "bronze dagger".startswith(weapon):
        weapon = "Bronze Dagger"
        damageMulti = 1.2
    elif "bronze sword".startswith(weapon):
        weapon = "Bronze Sword"
        damageMulti = 1.5
    elif "iron dagger".startswith(weapon):
        weapon = "Iron Dagger"
        damageMulti = 1.8
    elif "iron sword".startswith(weapon):
        weapon = "Iron Sword"
        damageMulti = 2.0
    elif "goblin cleaver".startswith(weapon):
        weapon = "Goblin Cleaver (Great Axe)"
        damageMulti = 2.5
    elif "dragon's bane".startswith(weapon):
        weapon = "Dragon's Bane (Great Sword)"
        damageMulti = 3.0
    else:
        print("weapon: {}, damage multiplier: {}".format(weapon, damageMulti))        
        return
    print("weapon: {}, damage multiplier: {}".format(weapon, damageMulti))        

    secWeapon = input("Define Weapon(Rusty Longsword, Bronze Sword, Dragon's Bane): ").lower()
    if "rusty butterknife".startswith(weapon):
        secWeapon = "Rusty Butterknife"
        sceDamageMulti = 0.5
    elif "rusty longsword".startswith(weapon):
        secWeapon = "Rusty Longsword"
        secDamageMulti = 1.0
    elif "bronze dagger".startswith(weapon):
        secWeapon = "Bronze Dagger"
        secDamageMulti = 1.2
    elif "bronze sword".startswith(weapon):
        secWeapon = "Bronze Sword"
        secDamageMulti = 1.5
    elif "iron dagger".startswith(weapon):
        secWeapon = "Iron Dagger"
        secDamageMulti = 1.8
    elif "iron sword".startswith(weapon):
        secWeapon = "Iron Sword"
        secDamageMulti = 2.0
    elif "goblin cleaver".startswith(weapon):
        secWeapon = "Goblin Cleaver (Great Axe)"
        secDamageMulti = 2.5
    elif "dragon's bane".startswith(weapon):
        secWeapon = "Dragon's Bane (Great Sword)"
        secDamageMulti = 3.0
    else:
        print("weapon: {}, damage multiplier: {}".format(secWeapon, secDamageMulti))        
        return
    print("weapon: {}, damage multiplier: {}".format(secWeapon, secDamageMulti))        



    helmet = input("Enter chosen helmet(leather, chainmail, bronze, iron, dragon scale):").lower()
    if "leather".startswith(helmet):
        helmet = "Leather"
        armor += 1
    elif "chainmail".startswith(helmet):
        helmet = "Chainmali"
        armor += 2
    elif "bronze".startswith(helmet):
        helmet = "Bronze"
        armor += 4
    elif "iron".startswith(helmet):
        helmet = "Iron"
        armor += 7
    elif "dragon scale".startswith(helmet):
        helmet = "Dragon's Scale"
        armor += 13
    else:
        helmet = "<unkown>"
    print("{} helmet, total armor -> {}% damage reduction".format(helmet, armor))

    chestplate = input("Enter chosen chestplate(leather, chainmail, bronze, iron, dragon scale):").lower()
    if "leather".startswith(chestplate):
        chestplate = "Leather"
        armor += 3
    elif "chainmail".startswith(chestplate):
        chestplate = "Chainmali"
        armor += 5
    elif "bronze".startswith(chestplate):
        chestplate = "Bronze"
        armor += 7
    elif "iron".startswith(chestplate):
        chestplate = "Iron"
        armor += 12
    elif "dragon scale".startswith(chestplate):
        chestplate = "Dragon's Scale"
        armor += 18
    print("{} chestplate, total armor -> {}% damage reduction".format(chestplate, armor))

    leggings = input("Enter chosen leggings(leather, chainmail, bronze, iron, dragon scale):").lower()
    if "leather".startswith(leggings):
        leggings = "Leather"
        armor += 2
    elif "chainmail".startswith(leggings):
        leggings = "Chainmail"
        armor += 3
    elif "bronze".startswith(leggings):
        leggings = "Bronze"
        armor += 5
    elif "iron".startswith(leggings):
        leggings = "Iron"
        armor += 10
    elif "dragon scale".startswith(leggings):
        leggings = "Dragon's Scale"
        armor += 16
    else:
        leggings = "<unknown>"
    print("{} leggings, total armor -> {}% damage reduction".format(leggings, armor))


    boots = input("Enter chosen boots(leather, chainmail, bronze, iron, dragon scale):").lower()
    if "leather".startswith(boots):
        boots = "Leather"
        armor += 1
    elif "chainmail".startswith(boots):
        boots = "Chainmail"
        armor += 2
    elif "bronze".startswith(boots):
        boots = "Bronze"
        armor += 4
    elif "iron".startswith(boots):
        boots = "Iron"
        armor += 7
    elif "dragon scale".startswith(boots):
        boots = "Dragon's Scale"
        armor += 13
    print("{} boots, total armor -> {}% damage reduction".format(leggings, armor))

    armVal = (100 - armor) / 100.0    
    
    
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

    first_turn()

def player_attack():
    global level, damageMulti, enemVal, enemHealth, lastTurn
    if level == 1:
        r1 = random.randint(1, 20)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        # print("You deal %s damage to the %s. The %s has %s hp left" % (damPlayAtt, enemVal, enemVal, enemHealth))
        print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"
    elif level == 2:
        r1 = random.randint(5, 15)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"
    elif level == 3:
        r1 = random.randint(5, 15)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        print("You deal {} damage to the {}. The {} has {} hp left".format(damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"
    if enemHealth <= 0:
        PlayerWin()
    if playHealt <= 0:
        PlayerDead()
        
def enemy_attack():
    global level, enemVal, enemHealth, enemDamMulti, playHealt, lastTurn
    if level == 1:
        r2 = random.randint(1, 10)
        damEnemAtt = r2 * enemDamMulti * armVal
        damEffect = damEnemAtt * armVal
        playHealt = playHealt - damEffect
        print(" ")
        # print("The %s attacks, dealing %s damage (reduced by armor to %s). You have %s hp left." % (enemVal, damEnemAtt, damEffect, playHealt))
        print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
        print(" ")
        lastTurn = "enemy"
    elif level == 2:
        r2 = random.randint(5, 15)
        damEnemAtt = r2 * enemDamMulti * armVal
        damEffect = damEnemAtt * armVal
        playHealt = playHealt - damEffect
        print(" ")
        print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
        print(" ")
        lastTurn = "enemy"
    elif level == 3:
        r2 = random.randint(5, 15)
        damEnemAtt = r2 * enemDamMulti * armVal
        damEffect = damEnemAtt * armVal
        playHealt = playHealt - damEffect
        print(" ")
        print("The {} attacks, dealing {:.2f} damage (reduced by armor to {:.2f}). You have {:.2f} hp left.".format(enemVal, damEnemAtt, damEffect, playHealt))
        print(" ")
        lastTurn = "enemy"
    if enemHealth <= 0.0:
        PlayerWin()
    if playHealt <= 0.0:
        PlayerDead()

def first_turn():
    global level
    r3 = random.randint(1, 2)
    if r3 == 1:
        print("It is your turn. Attack or flee?")
        decision = input(">>> ").lower()
        if "attack".startswith(decision):
            player_attack_melee()
        elif "flee".startswith(decision):
            sys.exit()

    elif r3 == 2:
        enemy_attack()
    main_combat()

def main_combat():
    if lastTurn == "enemy":
        print("It is your turn. Attack or flee?")
        decision = input(">>> ").lower()
        if "attack".startswith(decision):
            player_attack_melee()
        elif "flee".startswith(decision):
            sys.exit()
    elif lastTurn == "player":
        enemy_attack()


def PlayerWin():
    print("You have defeated the " + enemVal + "!\nPlay again or quit?")
    option = input(">>> ").lower()
    if "play again".startswith(option):
        set_values()
    else:
        sys.exit()

def PlayerDead():
    print("You have been defeated by the " + enemVal + "!\nPlay again or quit?")
    option = input(">>> ").lower()
    if "play again".startswith(option):
        set_values()
    else:
        sys.exit()


set_values()



while True:
    main_combat()

