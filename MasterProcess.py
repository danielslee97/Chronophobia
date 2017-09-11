from _Speech import *
import __2__._2lobby, __2__._2dining, __2__._2garage, __2__._2kitchen, \
       __2__._2den
import __3__._3bathroom, __3__._3bedroom, __3__._3storageRoom, __3__._3hallway
import __4__._4attic, Adjacency
import sys

def checkLocation(currentRoom, moveRoom, inventory):
            adj = Adjacency.Adjacency()
            adjCheck = adj.getDict()
            location = currentRoom.lower()
            destination = moveRoom
            if location == destination:
                return("You're already here.|" + "|" + currentRoom)
            else:
                possibleRooms = adjCheck[location]
                if destination in possibleRooms:
                    if destination == "kitchen":
                        if "kitchen key" in inventory:
                           currentLocation = destination
                           return(currentLocation)
                        else:
                            return("It's locked.|")
                    elif destination == "garage":
                        if "garage key" in inventory and \
                            "flashlight" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("It's locked, it looks dark too.|")
                    elif destination == "floor2Hallway":

                        if "hammer" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("You can't get through.|")
                    elif destination == "floor2Storage":
                        if "storage key" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("It's locked.|")
                    elif destination == "attic":
                        if "ladder" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("You can't get up there. Maybe you a ladder"\
                                   " would help.|")
                    elif destination == "mld":
                        if "burning curiosity" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("It's closed.|")
                    elif destination == "storage":
                        if "storage key" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("It's locked.|")
                    elif destination == "upstairs" or destination == "hallway":
                        if "hammer" in inventory:
                            currentLocation = destination
                            return(currentLocation)
                        else:
                            return("You can't go there.|")
                    elif (location == "lobby" or location == "diningroom"\
                    or location == "dining room" \
                    or location == "den" or location == "bedroom" \
                    or location == "bathroom"):
                        currentLocation = destination
                        return(currentLocation)
                    else:
                        currentLocation = destination

                    return currentLocation
                else:
                    return("You can't get there from here.|" + "|" +\
                             currentRoom)

def masterProcess(userInput, currentRoom, inventory):
    userInput = speech(userInput)
    output = ""
    if userInput[0] == "go":
        destination = userInput[-1]
        room = checkLocation(currentRoom, destination, inventory)
        if len(room) > 15:
            return(room)
        else:
            currentRoom = room

    if currentRoom == "lobby":
        output = __2__._2lobby.lobby(userInput, inventory)

    elif currentRoom == "diningroom" or currentRoom == "dining room":
        output = __2__._2dining.dining(userInput, inventory)

    elif currentRoom == "kitchen":
        output = __2__._2kitchen.kitchen(userInput, inventory)

    elif currentRoom == "den":
        output = __2__._2den.den(userInput, inventory)

    elif currentRoom ==  "garage":
        output = __2__._2garage.garage(userInput, inventory)

    elif currentRoom == "upstairs" or currentRoom == "hallway":
        output = __3__._3hallway.hallway(userInput, inventory)

    elif currentRoom == "bathroom":
        output = __3__._3bathroom.bathroom(userInput, inventory)

    elif currentRoom == "storage" or currentRoom == "closet":
        output = __3__._3storageRoom.storageRoom(userInput, inventory)

    elif currentRoom == "bedroom":
        output = __3__._3bedroom.bedroom(userInput, inventory)

    elif currentRoom == "attic":
        output = __4__._4attic.attic(userInput, inventory)
    
    else:
        return("The door is locked.")

    output = str(output) + "|" + str(currentRoom)
    return output



