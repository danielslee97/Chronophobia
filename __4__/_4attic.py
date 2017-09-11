#Attic

import _Speech
import _Nouns
from _Verbs import *
import __4__.journal


def attic(sentence=[], item=[]):
    noun = _Nouns.attic()
    verb = verbs()
    try:
        if sentence[0] == "go":
            return("You climb the ladder and slowly raise your gaze into the "\
                   "dusty room. As you walk towards the middle of the room, "\
                   "the floor creaks with every step you take. There's a "\
                   "window at the far end, a floor mirror with boxes "\
                   "surrounding it, and a wooden rocking chair in a corner "\
                   "that looks to be the last sight a white mannequin had as "\
                   "it sways above you, hung from a beam with a noose around "\
                   "its neck.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in noun:
            #LOOK/INSPECT/EXAMINE NOUNS
            if sentence[0] == verb[1]:
                #BOXES
                if sentence[-1] == noun[2] or sentence[-1] == noun[1]:
                    return("The boxes contain a broken framed picture, a "\
                          "leather journal, shattered light bulbs, a "\
                          "small vintage chest, and a tape recorder.|")
                #WINDOW
                elif sentence[-1] == noun[6]:
                    return("You look out the window."\
                          "You can't see anything. Nothing exists but the "\
                          "empty view of complete darkness. "\
                          "The sight reminds you of something.|")
                #MANNEQUIN
                elif sentence[-1] == noun[0]:
                    return("You stare into the lackless face of the mannequin."\
                          " Nothing happens.|")
                    
                #CHAIR
                elif sentence[-1] == noun[8]:
                    return("The chair has markings carved into its arm."\
                          " The handwriting looks familiar... "\
                          "It reads, 'ONE TOO MANY', with 6 tallies "\
                          "underneath it.|")

                #BOOK
                elif sentence[-1] == noun[7]:
                    return("The book is worn, it reads 'JOURNAL' across the "\
                           "top.  There are 2 entries.  One is entitled, "\
                           "'BLACK', the other, 'LOVE'.|")
                #MIRROR
                elif sentence[-1] == noun[16]:
                    return("You look at the mirror, but you see no "\
                           "reflection.|")
                #PHOTOS
                elif sentence[-1] == noun[11] or sentence[-1] == noun[12]:
                    return("It's a picture of you. You look happy, maybe with "\
                           "a family. You wonder how it got in its current "\
                           "state. It looks like it can be pried opened.|")
                #RECORDER
                elif sentence[-1] == noun[13] or \
                     sentence[-2] + sentence[-1] == noun[15]:
                    return("The tape recorder looks like it was smashed with "\
                           "force.|")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                           "happened.|")
            #OPEN NOUNS
            elif sentence[0] == verb[7]:
                #VINTAGE CHEST
                if sentence[-1] == noun[10]:
                    if "chest key" not in item:
                        return("The tiny chest is locked.|")
                    else:
                        return("You find what looks to be cocaine in a baggie."\
                              "|cocaine")
                #BOXES
                elif sentence[-1] == noun[2] or sentence[-1] == noun[1]:
                    return("The boxes contain a broken framed picture, a "\
                           " a leather journal, shattered light bulbs, a "\
                           "small vintage chest, and a tape recorder.|")
                #BOOK
                elif sentence[-1] == noun[7]:
                    return("The book is worn, it reads 'JOURNAL' across the "\
                           "top.  There are 2 entries.  One is entitled, "\
                           "'BLACK', the other, 'LOVE'.|")
                #WINDOW
                elif sentence[-1] == noun[6]:
                    return("You can't open the window, its sealed shut.|")
                #PHOTOS
                elif sentence[-1] == noun[11] or sentence[-1] == noun[12]:
                    return("You brake open the frame, dropping the family "\
                           "portrait and gaining a small key. It looks "\
                           "it can open some kind of lock.|key2")
                else:
                    return("You can't open the " + sentence[-1] + ".|")
            #READ NOUNS
            elif sentence[0] == verb[6]:                   
                #BOOK
                if sentence[-1] == noun[7] or sentence[-1] == noun[14]:
                    return("The book is worn, it reads 'JOURNAL' across the "\
                          "top.  There are 2 entries.  One is entitled, "\
                          "'BLACK', the other, 'LOVE'.|")
                else:
                    return("That's pointless.|")
            else:
                    return("You can't " + sentence[0] + " the " + \
                          sentence[-1] + ".|")
        #SNORT NOUNS
        elif sentence[0] == "snort":
            if sentence[-1] == "cocaine":
                if "cocaine" in item:
                    return("You get familiar sense of high that you can "\
                           "remember so vividly as guilt begins to grow "\
                           "inside you.|")
                else:
                    return("Huh?|")
            else:
                return("You can't " + sentence[0] + " the " + sentence[-1] + \
                      ".|")
        else:
            return("There's no " + sentence[-1] + " here.|")
    except:
        return("Huh?|")
