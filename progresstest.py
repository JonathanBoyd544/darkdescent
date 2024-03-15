from progress.bar import Bar
import time
from random import randint
import os

playerLvl = 0
xpForLevel = 50

print("These are your statistics:")
with Bar(" |=========== Level {} ============|\n".format(playerLvl), fill='=', max=xpForLevel) as bar:
    for i in range(xpForLevel):
        bar.next(randint(1, xpForLevel))
        time.sleep(1)
        os.system("cls")
    print("Success!")
    if bar >= xpForLevel:
        bar.set(0)