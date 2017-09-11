#Dining

import _Speech
import _Nouns
from _Verbs import *
import sys


def dining(sentence=[], item=[]):
    noun = _Nouns.dining()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You enter the dining room. There's a china closet, a table"\
                   ", a broken light ficture hanging from above table, and the"\
                   " doors to the kitchen, the den, and the lobby.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #TABLE
                if sentence[-1] == noun[0]:
                    return("It's wooden table.|")
                #CHINACLOSET
                elif sentence[-2] + sentence[-1] == noun[1]:
                    return("The china closet looks like it can be opened.|")
                #LIGHTS
                elif sentence[-1] == noun[2]:
                    return("The broken light ficture dangles from a single "\
                           "cord above the table.|")
                #NOTE
                elif sentence[-1] == noun[3]:
                    return("The note reads, 'You can look around, read, and "\
                           "interact with items. Try opening things.'|")                   
                #KITCHENDOOR
                elif sentence[-2] + sentence[-1] == noun[4]:
                    return("It's a door that leads to the kitchen.|")
                #DENDOOR
                elif sentence[-2] + sentence[-1] == noun[5]:
                    return("It's a door that leads to the den.|")
                #LOBBYDOOR
                elif sentence[-2] + sentence[-1] == noun[6]:
                    return("It's a door that leads to the lobby.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #OPEN NOUNS
            elif sentence[0] == verb[7]:
                #CHINACLOSET
                if sentence[-2] + sentence[-1] == noun[1] or \
                   sentence[-1] == noun[8]:
                    if "pliers" not in item:
                        return("The closest contains old silverware and "\
                               "broken dishes. You find a pair of pliers "\
                               "mysteriosuly in the closet. Looks like they'd"\
                               " come in handy.|pliers")
                    else:
                        return("The closest contains old silverware and "\
                               "broken dishes. You found the pliers in here "\
                               "previosuly.|")
                #KITCHENDOOR
                elif sentence[-2] + sentence[-1] == noun[4]:
                    if "kitchen key" not in item:
                        return("The door to the kitchen is locked.|")
                    else:
                        return("The door to the kitchen is unlocked.|")
                #DENDOOR
                elif sentence[-2] + sentence[-1] == noun[5]:
                    return("The door to the den is unlocked.|")
                #LOBBYDOOR
                elif sentence[-2] + sentence[-1] == noun[6]:
                    return("The door to the lobby is unlocked.|")
                else:
                    return("You can't open the " + sentence[-1] + ".|")
            #READ NOUNS
            elif sentence[0] == verb[6]:
                #NOTE
                if sentence[-1] == noun[3]:
                    return("The note reads, 'You can look around, read, and "\
                           "interact with items. Try opening things.'|")
                else:
                    return("That's pointless.|")
            else:
                return("You can't " + sentence[0] + " the " + sentence[-1] + \
                      ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
