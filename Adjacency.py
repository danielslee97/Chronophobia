
class Adjacency(): #Lists all rooms and which rooms they're adjacent to.
    def __init__(self):
        self.__attic = ("atticStair", "hallway")
        self.__atticStair = ("attic", "floor2Hall", "hallway")
        ####
        self.__upstairs = ("bathroom", "storage", "bedroom",
                             "attic", "closet", "lobby")
        self.__bathroom = "hallway"
        self.__masterBedroom  = "hallway"
        self.__storage = "hallway"
        self.__bedroom = "hallway"
        self.__floor2Stair = ("upstairs", "hallway", "lobby")
        ####
        self.__lobby  = ("upstairs", "diningroom", "den", "dining room")
        self.__den =  ("garage", "kitchen", "lobby")
        self.__garage = ("den")
        self.__diningroom = ("kitchen", "lobby", "basement")
        self.__kitchen = ("diningroom", "den", "dining room")
        ###
        self.__dictionary = {"attic":self.__attic,
        "atticStair":self.__atticStair, "upstairs":self.__upstairs,
        "hallway":self.__upstairs,
        "bathroom":self.__bathroom,
        "storage":self.__storage, "closet":self.__storage,
        "bedroom":self.__bedroom,
        "floor2Stair":self.__floor2Stair, "lobby":self.__lobby,
        "den":self.__den, "garage":self.__garage,
        "diningroom":self.__diningroom, "dining room":self.__diningroom,
        "kitchen":self.__kitchen}

    def getDict(self):
        return(self.__dictionary)
