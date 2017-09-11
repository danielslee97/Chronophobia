#bedroom


import _Speech
import _Nouns
from _Verbs import *


def bedroom(sentence=[], item=[]):
    noun = _Nouns.bedroom()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You leave the hallway and enter the bedroom. "\
                   "You notice the stripped "\
                   "sheetless bed. Beside it lies a drawe and a desk. A "\
                   "small closet is also present in the room.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #BED
                if sentence[-1] == noun[0] or sentence[-1] == noun[0]:
                    if "clown doll" not in item:
                        return("You look at the bed. The bed is messed up and "\
                               "ripped apart. There is a clown doll on the "\
                               "bed.|")
                    else:
                        return("You look at the bed. The bed is messed up and "\
                               "ripped apart.|")
                #DESK
                elif sentence[-1] == noun[1]:
                    return("You look at the desk. The desk has a wierd symbol "\
                           "in the middle. There is a sealed box attached to "\
                           "the desk. It seems you need a key to open it.|")
                #BOX
                elif sentence[-1] == noun[6]:
                    if "box key" not in item:
                        return("It seems that you need a key to open it.|")
                    else:
                        return("You use the key and you hear the click as the "\
                               "box open. You see another key inside.")
                #DRAWER
                elif sentence[-1] == noun[2]:
                    if "money" not in item:
                        return("You look at the drawer. It is opened and you "\
                               "see a pile of clothes inside along with "\
                               "money.|")
                    else:
                        return("You look at the drawer. It is opened and you "\
                               "see a pile of clothes inside.|")
                #CLOSET
                elif sentence[-1] == noun[3]:
                    return("The closet is bolted shut. You cannot open it.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                          "happened.|")
            #OPEN NOUNS
            elif sentence[0] == verb[7]:
                #BOX
                if sentence[-1] == noun[6]:
                    if "box key" in item:
                        return("You use the key and you hear the click as the "\
                               "box open. You see another key inside.|")
                    else:
                        return("You can't open the box. It is locked.|")
                #CLOSET
                elif sentence[-1] == noun[3]:
                    return("You cannot open the closet. It is bolted shut.|")
                else:
                    return("You can't open " + sentence[-1] + ".|")
            #GET NOUNS
            elif sentence[0] == verb[0]:
                #BOX
                if sentence[-1] == noun[6]:
                    return("You can't pick up the box. It's attached to the "\
                           "desk.|")
                #CLOTHES
                elif sentence[-1] == noun[8]:
                    return("The pile of clothes are useless. There is no point"\
                           " of picking it up.|")
                #MONEY
                elif sentence[-1] == noun[7]:
                    if "money" not in item:
                        return("You took the moeny.|money")
                    else:
                        return("You already have it in your inventory.|")
                #STORAGE KEY
                elif sentence[-1] == "key":
                    if "storage key" not in item:
                        return("You took the key.|storage key")
                    else:
                        return("You already have it in your inventory.|")
                #CLOWN DOLL
                elif sentence[-2] + sentence[-1] == noun[4] or \
                     sentence[-1] == noun[5]:
                    if "clown doll" not in item:
                        return(">>CLOWN DOLL ADDED TO INVENTORY<<|clown doll")
                    else:
                        return("You already have it in your inventory.|")
                else:
                    return("You can't pick up " + sentence[-1] + ".|")
            else:
                return("You can't " + sentence[0] + " the " + \
                       sentence[-1] + ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
