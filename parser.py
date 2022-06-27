# from nltk import CFG, Production, nonterminals
# grammar = CFG.fromstring(
#     """
        
#       S -> STEM OPTIONS
#       OPTIONS -> OPTION | 
#       OPTION -> KEY | DISTRACTOR
#       KEY -> KEY_SIGN 
#       DISTRACTOR -> 
#       SEMICOLONE -> ';'
#       KEY_SIGN -> '[*]'
#       DISTRACTOR_SIGN -> '[]'
      
#       HASH -> '#'
#     """
# )

from enum import Enum

class Token(Enum):
    STEM = 0
    OPTIONS = 1
    OPTION = 2
    KEY = 3
    KEY_SIGN = 4
    CONTENT = 5
    DISTRACTOR = 6
    DISTRACTOR_SIGN = 7
    HASH = 8
    