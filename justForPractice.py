from dataclasses import dataclass


@dataclass
class Asdf():
    name : str = "KANG"
    def __repr__(self) -> str:
        return self.name + "입니다"
    
    

print(repr(a))