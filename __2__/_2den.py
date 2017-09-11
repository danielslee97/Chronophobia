#Den/Living Room

import _Speech
import _Nouns
from _Verbs import *
import sys


def den(sentence, item):
    noun = _Nouns.den()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You walk into the living room. You see a couch, a tv, "\
                   "and a toy box. The living room is connected to the "\
                   "lobby, garage, kitchen, and dining room.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #COUCH
                if sentence[-1] == noun[0]:
                    if "kitchen key" not in item:
                        return("You look at the couch. It is ripped and torn. "\
                               "You see a shining light on the couch. Looking "\
                               "closely you see that it is a key sticking out "\
                               "of one of holes of the couch.|")
                    else:
                        return("You look at the couch. It is ripped and torn.|")
                #TV
                elif sentence[-1] == noun[1] or sentence[-1] == noun[2]:
                    return("You look at the tv. It's stuck on a channel "\
                           "of static.|")
                #TOYBOX
                elif sentence[-2] + sentence[-1] == noun[7] or \
                     sentence[-1] == noun[16]:
                    if "toy magnet" not in item:
                        return("You look at the toy box. It is open and you "\
                               "see a bunch of toys inside. There is a toy "\
                               "magnet. That seems useful for later.|")
                    else:
                        return("You look at the toy box. It is opened and you "\
                               "see a bunch of toys inside.|")
                #MIRROR
                elif sentence[-1] == noun[10]:
                    return("You look at the mirror. You see your own "\
                           "reflection.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #GET NOUNS
            elif sentence[0] == verb[0]:
                #TOY MAGNET
                if sentence[-1] == noun[8] or \
                   sentence[-2] + sentence[-1] == noun[9]:
                    if "toy magnet" not in item:
                        return("You picked up the toy magnet from the box."\
                               "|toy magnet")
                #TOYS
                elif sentence[-1] == noun[6]:
                    return("The toys are useless. There is no point picking "\
                           "them up.|")
                #KITCHEN KEY
                elif sentence[-1] == noun[11]:
                    if "kitchen key" not in item:
                        return("You grab the key that is sticking out of the "\
                               "couch."\
                               "|"\
                               "kitchen key")
                    else:
                        return("You already have the kitchen key in your "\
                               "inventory.|")
                else:
                    return("You can't pick up the " + sentence[-1] + '.')
            else:
                return("You can't " + sentence[0] + " the " + \
                       sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
