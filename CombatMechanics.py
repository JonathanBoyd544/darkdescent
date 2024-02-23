import random
from random import randint
import sys
random.seed(None)

level = 0
damageMulti = 0
damPlayAtt = 0
damEnemAtt = 0
enemHealth = 0
enemDamMulti = 0
playHealt = 100
enemVal = "not defined"
lastTurn = "not defined"

def set_values():
    global level, damageMulti, enemHealth, enemDamMulti, enemVal
    
    level = input("Define Level: ")
    if level == "1":
        level = 1
    elif level == "2":
        level = 2
    elif level == "3":
        level = 3
    else:
        return
    
    weapon = input("Define Weapon(Rusty Longsword, Bronze Sword, Dragon's Bane): ")
    if weapon == "Rusty Longsword":
        damageMulti = 1
    elif weapon == "Bronze Sword":
        damageMulti = 1.5
    elif weapon == "Dragon's Bane":
        damageMulti = 3
    else:
        return
    
    enemy = input("Define Enemy: ")
    if enemy == "goblin":
        enemVal = "Goblin"
        if level == 1:
            enemHealth = 30
            enemDamMulti = 0.75
        elif level == 2:
            enemHealth = 45
            enemDamMulti = 1
        elif level == 3:
            enemHealth = 55
            enemDamMulti = 1.5
    else:
        return
    
    first_turn()

def player_attack_melee():
    global level, damageMulti, enemVal, enemHealth, lastTurn
    if level == 1:
        r1 = random.randint(1, 10)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        print("You deal %s damage to the %s. The %s has %s hp left" % (damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"
    elif level == 2:
        r1 = random.randint(5, 15)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        print("You deal %s damage to the %s. The %s has %s hp left" % (damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"
    elif level == 3:
        r1 = random.randint(5, 15)
        damPlayAtt = r1 * damageMulti
        enemHealth = enemHealth-damPlayAtt
        print("You deal %s damage to the %s. The %s has %s hp left" % (damPlayAtt, enemVal, enemVal, enemHealth))
        lastTurn = "player"

def enemy_attack():
    global level, enemVal, enemHealth, enemDamMulti, playHealt, lastTurn
    if level == 1:
        r2 = random.randint(1, 10)
        damEnemAtt = r2 * enemDamMulti
        playHealt = playHealt - damEnemAtt
        print(" ")
        print("The %s attacks, dealing %s damage. You have %s hp left." % (enemVal, damEnemAtt, playHealt))
        print(" ")
        lastTurn = "enemy"
    elif level == 2:
        r2 = random.randint(5, 15)
        damEnemAtt = r2 * enemDamMulti
        playHealt = playHealt - damEnemAtt
        print(" ")
        print("The %s attacks, dealing %s damage. You have %s hp left." % (enemVal, damEnemAtt, playHealt))
        print(" ")
        lastTurn = "enemy"
    elif level == 3:
        r2 = random.randint(5, 15)
        damEnemAtt = r2 * enemDamMulti
        playHealt = playHealt - damEnemAtt
        print(" ")
        print("The %s attacks, dealing %s damage. You have %s hp left." % (enemVal, damEnemAtt, playHealt))
        print(" ")
        lastTurn = "enemy"

def first_turn():
    global level
    r3 = random.randint(1, 2)
    if r3 == 1:
        print("It is your turn. Attack or flee?")
        decision = input(">>> ").lower()
        if decision == "attack":
            player_attack_melee()
        elif decision == "flee":
            sys.exit()

    elif r3 == 2:
        enemy_attack()
    main_combat()

def main_combat():
    if lastTurn == "enemy":
        print("It is your turn. Attack or flee?")
        decision = input(">>> ").lower()
        if decision == "attack":
            player_attack_melee()
        elif decision == "flee":
            sys.exit()
    elif lastTurn == "player":
        enemy_attack()


set_values()

while True:
    main_combat()