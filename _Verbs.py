## Gunczler, Ron; Hoover, David; Vasilakis, Troy; and Lee, Seung Woo
## A53, A52, A53, and A53
## HRCSMD
## Keyword List Module


KEYWORDS={
    
    # Get phrases
    "acquire":["accumulate", "acquire", "amass", "annex", "attain", "bag",
               "capture", "carry", "cop", "gain", "garner", "get", "glom",
               "grab", "grasp", "grip", "hold", "nab", "net", "obtain",
               "pickup", "procure", "reacquire", "reattain", "recapture",
               "regain", "secure", "take", "win"],

    # Look phrases
    "inspect":["analyze", "apprehend", "audit", "canvas", "canvass",
               "categorize", "check", "classify", "comprehend", "decipher",
               "dissect", "examine", "explore", "glanceat", "glanceover",
               "inspect", "investigate", "look", "lookat", "lookover",
               "notice", "observe", "oversee", "perceive", "pickover",
               "plumb", "probe", "reinspect", "reinvestigate", "rereview",
               "research", "resurvey", "scrutinize", "see", "study",
               "survey", "view", "watch"],

    # Deploy phrases
    "use":["apply", "deploy", "employ", "exert", "operate", "reapply",
           "reuse", "use"],

    # Discard phrases
    "drop":["abort", "abrogate", "annul", "blow", "bobble",
            "bungle", "disburse", "discard", "discontinue", "dissipate", "drop",
            "expend", "foozle", "forfeit", "forkover", "fritter",
            "fritteraway", "fumble", "giveup", "invalidate", "layout",
            "lose", "nullify", "plunkdown", "relinquish", "return",
            "runthrough", "scrap", "squander", "surrender", "throw",
            "throwaway", "throwdown", "void", "waste", "writeoff"],

    # Entry phrases
    "go":["accelerate", "advance", "approach", "bail", "bear", "come",
          "course", "cross", "enter", "fare", "follow", "go", "head", "hike",
          "journey", "lead", "march", "move", "navigate", "near", "pace",
          "pass", "perambulate", "peregrinate", "proceed", "progress",
          "run", "speed", "track", "traipse", "tramp", "transit", "travel",
          "tread", "walk", "wend"],

    # Exit phrases
    "leave":["abandon", "escape", "exit", "flee", "fly", "leave"],

    # Review phrases
    "read":["browse", "combthrough", "delve", "delveinto", "leafthrough",
            "parse", "peruse", "poreover", "read", "reread", "review",
            "scan", "search", "searchthrough", "skim", "thumbthrough",
            "understand"],

    # Open phrases
    "open":["disengage", "ease", "loosen", "open",
            "release", "slip", "unblock", "unclog", "unclose", "unstop"],

    # Activation phrases
    "turn on":["actuate", "catalyze", "launch", "power", "reactivate",
              "start", "trigger", "trip", "turnon"], 

    # Deactivation phrases
    "turn off":["arrest", "cut", "cutoff", "cutout", "deactivate", "halt",
               "kill", "repress", "shutoff", "stop", "suppress", "turnoff"],
    
    # Toggle phrases
    "toggle":["flip", "switch", "toggle"],
    
    # Caress phrases
    "caress":["bill", "canoodle", "caress", "coddle", "cradle", "cuddle",
              "embrace", "enfold", "feelup", "gentle", "hug", "knead",
              "love", "massage", "neck", "nestle", "nose", "nuzzle", "pat",
              "paw", "pet", "rub", "snuggle", "spoon", "stroke"]
}


VERBS = ["acquire", "inspect", "use", "drop", "go", "leave", "read",
         "open", "turn on", "turn off", "toggle", "caress"]


def check(word):
    for key in KEYWORDS:
        if word in KEYWORDS[key]:
            return key
    return word

def verbs():
    return (VERBS)

