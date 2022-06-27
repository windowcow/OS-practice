# from enum import Enum


# class MulChoiceToken(Enum):
#     TITLE = 0
#     DISTRACTION = 1
#     KEY = 2

from nltk import CFG, Production, nonterminals
grammar = CFG.fromstring(
    """
        
      S -> STEM OPTIONS
      OPTIONS -> OPTION | 
      OPTION -> KEY | DISTRACTOR
      KEY -> KEY_SIGN 
      DISTRACTOR -> 
      SEMICOLONE -> ';'
      KEY_SIGN -> '[*]'
      DISTRACTOR_SIGN -> '[]'
      
      HASH -> '#'
    """
)

print(repr(grammar))
