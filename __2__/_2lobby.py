import _Nouns
import _Verbs

def lobby(userInput, inventory):
    nouns = _Nouns.lobby()
    verbs = _Verbs.verbs()
    sentence = userInput
    try:
        if sentence[0] == "go":
            return("You find yourself in a dark room."\
                   "Upon examining your surroundings, you seem"\
                   " to be in what looks like a fairly old house. Partially "\
                   "because"\
                   " of the smell of old paintings, and partially because of "\
                   "the woodworks."\
                   " In this room, there's three doors, one on either side of "\
                   "the stairs and one that has three locks on it. There is"\
                   " a large, wooden closet and a boarded-up staircase. There "\
                   "is also a"\
                   " table with a lamp. The doors lead to a den and a dining "\
                   "room. And a front door looking like your only way out seems"\
                   " to be locked shut by 3 locks.|")
        elif sentence[0] == '':
            return('|')
        elif sentence[-1] in nouns:
            #Look/Examine/Inspect
            if sentence [0] == "inspect":
                #Stairs
                if sentence[-1] == "stair" or sentence[-1] == "stairs" or \
                   sentence[-1] == "staircase":
                    return("You look at the stairs. It is boarded up.|")
                #Table
                elif sentence[-1] == "table":
                    return("The table is ornately crafted from what seems "\
                          "to you like oak. There's a lamp and a note on"\
                          " the table.|")
                elif sentence[-1] == "room" or sentence[-1] == "around":
                    return("You find yourself in a dark room."\
                           "Upon examining your surroundings, you seem"\
                           " to be in what looks like a fairly old house. "\
                           "Partially because of the smell of old paintings, "\
                           "and partially because of the woodworks."\
                           " In this room, there are two doors, one on "\
                           "either side of the stairs, a large, wooden "\
                           "closet and a boarded-up staircase. There is also "\
                           "a table with a lamp. The doors lead to a den "\
                            "and a dining room. There is also the front door "\
                           "that is locked.|")
                #Escape door
                elif sentence[-1] == "door" or sentence[-1] == "lockeddoor":
                    return("The door is locked with 3 locks. It seems you "\
                           "need three keys to open it.|")
                #Note
                elif sentence[-1] == "note":
                    return("I'm sure you're wondering what's going on right"\
                           " now, and that's fine. All you need to know is "\
                           "[the note has had water on it and some letters"\
                           " have been smudged out] but I'm sure you're"\
                           " going to be fine. Just tell yourself what to"\
                           " do, and what to do it to, and you can make it."\
                           " You're our only hope, so stay determined!"\
                           " PS: If something made of two words isn't working,"\
                           " try mushing them together. That might work. Also,"\
                           " be on the look out for a flashlight, you're "\
                           "gonna need it.|")
                #Closet
                elif sentence[-1] == "closet":
                    return("The closet is fairly large and made of a fine"\
                           " wood. On the inside there are a couple of dusty"\
                           "coats and a wire coat hanger. There's also a "\
                           "flashlight resting at the bottom that you think "
                           "you should take just extra incase.|")

                #Lamp
                elif sentence[-1] == "lamp":
                    return("The lamp looks very fancy. It's made of stained"\
                            " glass, and the power cord's been severed from"\
                            " the base. Doesn't look like this'll be lighting"\
                            " anything anytime soon.|")

                #Stairs
                elif sentence[-1] == "stairs":
                    if "hammer" in inventory:
                        return("The hammer has allowed you to remove the"\
                                " blockage from the stairs, allowing access"\
                                " to the second floor. Looks spooky up there.|")
                    else:
                        return("The stairs are blocked by a bunch of boards"\
                                " nailed to them. Perhaps you could remove"\
                                " them with a tool of some kind?|")

                #Paintings
                elif sentence[-1] == "paintings":
                    return("The paintings hanging in the Lobby show scenes of"\
                           " cherubs and people frolicking in fields. Or are"\
                           " the cherubs terrorizing the people? You can't"\
                           " tell.|")
                #Flashlight
                elif sentence[-1] == "flashlight":
                    return("It's a flashlight. It seems fairly new.")
                else:
                    return("You stare at the " + sentence[-1] + ". Nothing "+\
                           "happened.|")
            #Take
            elif sentence[0] == "acquire":
                if sentence[-1] == "hanger" or sentence[-1] == "wire hanger":
                    if "wire hanger" not in inventory:
                        return("You take the wire hanger from the closet."\
                                "|wire hanger")
                    else:
                        return("You already have the hanger.|")

                elif sentence[-1] == "flashlight":
                    if "flashlight" not in inventory:
                        return("You take the flashlight.|flashlight")
                    else:
                        return("You already took the flashlight.|")
                else:
                    return("You can't pick up the " + sentence[-1] + ".|")
            #Use
            elif sentence[0] == "use":
                if sentence[-1] == "lamp":
                    return("You try to use the lamp, but nothing happens.|")
                else:
                    return("You can't use the " + sentence[-1] + ".|")
            #Open
            elif sentence[0] == "open":
                #Escape door
                if sentence[-2] + sentence[-1] == "frontdoor" or \
                   sentence[-1] == "door":
                    if "key1" in inventory and "key2" in inventory and \
                       "key3" in inventory:
                        return("| ")
                    else:
                        return("The door remains locked shut.|")
                else:
                    return("You can't open the " + sentence[-1] + ".|")
            
            #Read
            elif sentence[0] == "read":
                if sentence[-1] == "note":
                    return("I'm sure you're wondering what's going on right"\
                           " now, and that's fine. All you need to know is "\
                           "[the note has had water on it and some letters"\
                           " have been smudged out] but I'm sure you're"\
                           " going to be fine. Just tell yourself what to"\
                           " do, and what to do it to, and you can make it."\
                           " You're our only hope, so stay determined!"\
                           " PS: If something made of two words isn't working,"\
                           " try mushing them together. That might work.|")
                else:
                    return("You can't read the " + sentence[-1] + ".|")
                
            else:
                return("Huh?|")
        else:
            return("Huh?|")
    except IndexError:
        return("Huh?|")
