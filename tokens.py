# Content of Stem : between '#' and '\n[]'
# Content of Key : between'\n[]' or between '#' and 
# Content of Stem : between '#' and '\n[]'


from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    STEM = 0
    OPTIONS = 1
    OPTION = 2
    KEY = 3
    KEY_SIGN = 4
    
    CONTENT = 5
    DISTRACTOR = 6
    DISTRACTOR_SIGN = 7
    HASH = 8
    
@dataclass
class Token:
    type: TokenType
    value: any = None
    
    def __repr__(self) -> str:
        return self.type.name + (f":{self.value}" if self.value != None else "has no value yet")

