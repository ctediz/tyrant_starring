import random
import os
import sys

# tyrant class
class Tyrant:
    star = 0
    meso = 0.0
    booms = 0
    target = 0
    consecFails = 0
    attempts = 0

    def __init__(self, target):
        self.target = target

    def printTyrant(self):
        print "Tyrant stars " + str(self.star)
        print("Meso cost " +"{:,}".format(self.meso))
        print "Booms " + str(self.booms)
        print "Attempts " + str(self.attempts)

# does checks for rolls
def rolling(passChance, boom, actual, tyrant):
    tyrant.attempts += 1
    
    # free pass on 2 consecutive fails
    if(tyrant.consecFails == 2):
        tyrant.star += 1
        tyrant.consecFails = 0
        return
    
    # pass
    if(actual < passChance*10):
        tyrant.star += 1
        consecFails = 0
    # boom
    elif(actual > 999-(boom*10)):
        tyrant.star = 0
        tyrant.booms += 1
        tyrant.consecFails = 0        
    # fail
    else:
        if(tyrant.star != 0):
            tyrant.star -= 1
        tyrant.consecFails += 1
            
# Sets up tyrant checks for rolling function
def starChance(roll, tyrant):
    # cost of tyrant star
    tyrant.meso += 55832200
    if(tyrant.star == 0 or tyrant.star == 1):
        rolling(50,0,roll,tyrant)
    elif(tyrant.star == 2):
        rolling(45,0,roll,tyrant)
    elif(tyrant.star == 3 or tyrant.star == 4):
        rolling(40,0,roll,tyrant)
    elif(tyrant.star == 5):
        rolling(40,1.8,roll,tyrant)
    elif(tyrant.star == 6):
        rolling(40,3,roll,tyrant)
    elif(tyrant.star == 7):
        rolling(40,6,roll,tyrant)        
    elif(tyrant.star == 8):
        rolling(40,9.5,roll,tyrant)    
    elif(tyrant.star == 9):
        rolling(37,9.5,roll,tyrant)        
    elif(tyrant.star == 10):
        rolling(35,13,roll,tyrant)    
    elif(tyrant.star == 11):
        rolling(35,16.3,roll,tyrant)
    elif(tyrant.star == 12):
        rolling(3,48.5,roll,tyrant)
    elif(tyrant.star == 13):
        rolling(2,49,roll,tyrant)
    elif(tyrant.star == 14):
        rolling(1,49.5,roll,tyrant)

# Gets star target from argument list
def getStar():
    if(len(sys.argv) > 1):
        try:
            attempt = (int(sys.argv[1]))
            if(attempt < 0 or attempt > 15):
                raise ValueError()
            return attempt
        except ValueError:
            print "Invalid star target; using 10"
            return(10)
        
# ------------------------------------ #
tyrant = Tyrant(getStar())
rng = random.SystemRandom()

while(tyrant.star != tyrant.target):
    starChance(rng.randint(0,999), tyrant)

tyrant.printTyrant()
