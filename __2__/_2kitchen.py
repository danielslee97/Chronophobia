#Kitchen

import _Speech
import _Nouns
from _Verbs import *
import sys


def kitchen(sentence=[], item=[]):
    noun = _Nouns.kitchen()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You walk into the kitchen leaving the door to the dining "\
                   "room opened and there's another entrnace to the den. "\
                   "The kitchen is bare, only containing a refridgerator, an "\
                   "oven, a sink, and a cabinet.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #REFRIDGERATOR
                if sentence[-1] == noun[0] or sentence[-1] == noun[1]:
                    return("You look at the refridgerator. It is open and you "\
                           "find rotten food inside. On the outside, there "\
                           "is a note.|")
                #FOOD
                elif sentence[-1] == noun[2]:
                    return("You look at the rotten food. It smells bad.|")
                #NOTE
                elif sentence[-1] == noun[6]:
                    return("You look at the note. It reads 'The garage key "\
                           "fell into the sink drainage. Call a plumber.'|")
                #OVEN
                elif sentence[-1] == noun[3]:
                    return("You look ath the oven. It seems to be broken.|")
                #SINK
                elif sentence[-1] == noun[4]:
                    return("You look at the sink. It seems to be broken.|")
                #DRAIN
                elif sentence[-1] == noun[5]:
                    return("You look down the drain. There seems to be "\
                           "a key stuck inside but it is to far in.|")
                #CABINET
                elif sentence[-1] in noun[7]:
                    return("You look at the cabinet. It is opened. You look "\
                           "inside and all you see are combwebs.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #GET NOUNS
            elif sentence[0] == verb[0]:
                #GARAGE KEY
                if sentence[-1] == noun[8] or \
                   sentence[-2] + sentence[-1] == noun[9]:
                    if "garage key" not in item:
                        if "wire hanger" in item and "pliers" in item and \
                           "toy magnet" in item:
                            return("You use the pliers to straighten the "\
                                   "hanger and attach the toy magnet to "\
                                   "the end of the straightened hanger. You "\
                                   "put it inside the drainage and the key "\
                                   "gets attached to it. You pick up the key."\
                                   "|"\
                                   "garage key")
                        else:
                            return("You can't reach down the drain.|")
                    else:
                        return("You already have the garage key in your "\
                               "inventory.|")
                #REFRIDGERATOR
                elif sentence[-1] == noun[0] or sentence[-1] == noun[1]:
                    return("You can't pick up the refridgerator. It is too "\
                           "heavy.|")
                #FOOD
                elif sentence[-1] == noun[2]:
                    return("You can't pick up the food. It's rotten and "\
                           "disgusting.|")
                else:
                    return("You can't pick up the " + sentence[-1] + '.|')
            #READ NOUNS
            elif sentence[0] == verb[6]:
                #BOOK
                if sentence[-1] == noun[6]:
                    return("The note reads 'The garage key fell into the sink "\
                           "drain. Call a plumber.'|")
                else:
                    return("That's pointless.")
            else:
                return("You can't " + sentence[0] + " the " + \
                      sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
