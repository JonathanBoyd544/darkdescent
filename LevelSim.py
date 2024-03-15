##### Leveling Simulation #####

import os
import sys
import time
from progress.bar import Bar

xpForLevel = 25
class Player:
    def __init__(self):
        self.level = 0
        self.maxhealth = 100
        self.health = self.maxhealth
        self.damageMulti = 0

    def playerStats():
        global xpForLevel, self
        print("Health: {}/{}".format(self.health, self.maxhealth))
        print("Power: {}".format(self.damageMulti))
        with Bar(" |=========== Level {} ============|\n".format(self.level), fill='=', max=xpForLevel) as bar:
            for i in range(xpForLevel):
                    # print("xp")
                    # print("These are your statistics:")
                    bar.next(15)
                    time.sleep(2)
            if bar >= xpForLevel:
                bar.next(-10000)


                

# def showStats():
#     global tof, xpForLevel, self
#     # levelProg()
#     print("Health: {}/{}".format(self.health, self.maxhealth))
#     print("Power: {}".format(self.damageMulti))
    
#     with Bar(" |=========== Level {} ============|\n".format(self.level), fill='=', max=xpForLevel) as bar:
            # for i in range(xpForLevel):
            #     # while tof == "true":
            #     print("xp")
            #     # os.system('cls')
            #     print("These are your statistics:")

            #     bar.next(randint(1, xpForLevel))
            #     sleep(1)
            # if bar >= xpForLevel:
            #     bar.finish()
                
#                 # if Bar == 'FINISHED':
#                 print("\n \nHealth: {}/{}".format(self.health, self.maxhealth))
#                 print("Power: {}".format(self.damageMulti))
#                 tof = "false"
                    
#                 increment = input("\nIncrement Bar?: ")
#                 if increment == "n":
#                     pass
#                 else:
#                     amount = randint(1, 100)
#                     amount = input("How Much?: ")
#                     amount = int(amount)
#                     incamount = amount 
#                     bar.next(incamount)
#                     pass
                
playerStats()