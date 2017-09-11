#Garage

import _Speech
import _Nouns
from _Verbs import *


def garage(sentence, item):
    noun = _Nouns.garage()
    verb = verbs()
  #  try:
    if sentence[0] == "go":
        return("You enter the garage. There's an old parked car, a pile "\
               "of tools, and a lawnmower in the corner.|")
    elif sentence[0] == '':
            return('|')
    elif sentence[-1] in noun:
        #LOOK/INSPECT/EXAMINE NOUNS
        if sentence[0] == verb[1]:
            #TOOLS
            if sentence[-1] == noun[3]:
                if "hammer" not in item:
                    return("You look at the pile of tools. There is a "\
                           "hammer in the pile. That seems useful for "\
                           "later.|")
                else:
                    return("You look at the pile of tools. This is where "\
                           "you got the hammer from.|")
            #LAWNMOWER
            elif sentence[-1] == noun[1]:
                return("You look at the lawnmower. It seems to be broken "\
                       "as it does not start up.|")

            #CAR
            elif sentence[-1] == noun[2]:
                if "key1" not in item:
                    return("You look at the car. You see that the windows "\
                           "of the car are all broken. There is a key "\
                           "laying around on the driver's seat of the car.|")
                else:
                    return("You look at the car. You see that the windows "\
                           "of are all broken.|")
            else:
                return("You stare at the " + sentence[-1] + ". Nothing "+\
                       "happened.|")
        #GET NOUNS
        elif sentence[0] == verb[0]:
            #KEY
            if sentence[-1] == noun[4]:
                if "key1" not in item:
                    return("You carefully grab the key from the drive's "\
                           "seat.|key1")
                else:
                    return("You already have the key in your inventory.|")
            #HAMMER
            if sentence[-1] == noun[0]:
                if "hammer" not in item:
                    return("You grab the hammer from the pile of tools.|hammer")
                else:
                    return("You already have the hammer in your inventory.|")
            else:
                return("You can't open the " + sentence[-1])
        else:
            return("You can't " + sentence[0] + " the " + sentence[-1] + \
                   ".|")
    else:
        return("There's no " + sentence[-1] + " here.|")
 #   except:
  #      return("Huh?|")

