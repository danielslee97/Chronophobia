#Storage Room

import _Speech
import _Nouns
from _Verbs import *
import sys


def storageRoom(sentence=[], item=[]):
    noun = _Nouns.storage()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("The storage room is pitch black... You turn on the light "\
                   "and you see a worn out room with the paint chipping "\
                   "away. One large rusted pipe rests above you and it looks "\
                   "like the place "\
                   "will collapse soon. There is a box in the middle of the "\
                   "room.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #BOX
                if sentence[-1] == noun[1]:
                    return("You look at the box. It seems like there is "\
                           "something inside.|")
                #PIPE
                elif sentence[-1] == noun[5]:
                    if "key3" in item:
                        return("You look at the pipe. It's very rusty. "\
                               "Water continues to drop down from it.|")
                    else:
                        return("You look at the pipe. It's very rusty. "\
                               "Water continues to drop down from it. It "\
                               "looks like there's a key resting on top of it.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #OPEN NOUNS
            elif sentence[0] == verb[7]:
                #BOX
                if sentence[-1] == noun[4]:
                    if "ladder" not in item:
                        return("You open the box. There is a ladder. It seems "\
                               "like it will be useful later on.|")
                    else:
                        return("You open the box. It is empty.|")
                else:
                    return("You can't open the " + sentence[-1] + ".|")
            #TAKE ITEM
            elif sentence[0] == verb[0]:
                #LADDER
                if sentence[-1] == "ladder":
                    if "ladder" not in item:
                        return("You take the ladder.|ladder")
                    else:
                        return("You already have the ladder.")
                #KEY3
                elif sentence[-1] == "key":
                    if "key3" not in item:
                        return("You take the key.|key3")
                    else:
                        return("You already have the key.")
                else:
                    return("You can't " + sentence[0] + " the " + \
                          sentence[-1] + ".|")
            else:
                    return("You can't " + sentence[0] + " the " + \
                          sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
