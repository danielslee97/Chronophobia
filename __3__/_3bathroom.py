#Second floor bathroom

import _Speech
import _Nouns
from _Verbs import *


def bathroom(sentence=[], item=[]):
    noun = _Nouns.bathroom()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You leave the hallway and enter the bathroom. "\
                   "The bathroom only houses a bathtub, a toilet, and a "\
                   "shattered mirror above the sink.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #BATHTUB
                if sentence[-2] + sentence[-1] == noun[3] or \
                   sentence[-1] == noun[4] or sentence[-1] == "bathtub":
                    if "rubber duck" not in item:
                        return("You look at the bath tub. It seems to be "\
                               "broken as the water does not run. There is "\
                               "something in thr drainage. It seems to be a "\
                               "key.|")
                    else:
                        return("You look at the bath tub. It seems to be "\
                               "broken as the water does not run.|")
                #TOILET
                elif sentence[-1] == noun[2]:
                    return("You look into the toilet. There is nothing "\
                           "important to see.|")
                #SINK
                elif sentence[-1] == noun[5]:
                    if "toothbrush" not in item:
                        return("You look at the sink. It seems to be "\
                               "broken as the water does not run. There is "\
                               "a toothbrush on the sink.|")
                    else:
                        return("You look at the sink. It seems to be broken "\
                               "as the water does not run.|")
                #MIRROR
                elif sentence[-1] == noun[6]:
                    return("You look at the mirror. It's too shattered to see "\
                           "anything.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #GET NOUNS
            elif sentence[0] == verb[0]:
                #DUCK
                if sentence[-1] == noun[7]:
                    if "rubber duck" not in item:
                        return("It was just a rubber duck."\
                               " You took the duck.|rubber duck")
                    else:
                        return("You already have it in your inventory.|")
                #TOOTHBRUSH
                elif sentence[-2] + sentence[-1] == noun[0] or \
                   sentence[-1] == noun[0]:
                    if "toothbrush" not in item:
                        return("You took the toothbrush.|toothbrush")
                    else:
                        return("You already have it in your inventory.|")
                else:
                   return("You can't take the " + sentence[-1] + ".|")
            else:
                 return("You can't " + sentence[0] + " the " + \
                        sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
