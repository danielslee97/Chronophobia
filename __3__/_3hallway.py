#Hallway


import _Speech
import _Nouns
from _Verbs import *


def hallway(sentence=[], item=[]):
    noun = _Nouns.hallway()
    verb = verbs
    try:
        if sentence[0] == "go":
            return("You enter the second floor hallway as the old floor "
                   "creaks with your every footstep. There are doors that "\
                   "seem to lead to only a single bedroom, a storage closet, "\
                   "and a bathroom. There's also an entrance to the attic "\
                   "that looks to be out of your reach.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #OPEN NOUNS
            elif sentence[0] == verb[7]:
                #STORAGE ROOM
                if sentence[-1] == noun[1]:
                    if "storage key" not in item:
                        return("The door to the storage room is locked.|")
                    else:
                        return("You walk into the storage room.|")
                else:
                    return("You can't open the " + sentence[-1] + ".|")
            #GO IN ROOMS
            elif sentence[0] == verb[4]:                   
                #STORAGE ROOM
                if sentence[-1] == noun[1]:
                    if "storage key" not in item:
                        return("The storage room is locked.|")
                    else:
                        return("You walk into the storage room.|")
                #BATHROOM
                elif sentence[0] == noun[2]:
                    return("You walk into the bathroom.|")
                #BEDROOM
                elif sentence[0] == noun[3]:
                    return("You walk into the bedroom.|")
                #ATTIC
                elif sentence[0] == noun[7]:
                    if "ladder" not in item:
                        return("The door to the attic to too high up.|")
                    else:
                        return("You use the ladder and climb up to the attic.|")
                else:
                    return("You can't go into " + sentence[-1] + ".|")
            else:
                return("You can't " + sentence[0] + " the " + \
                       sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
