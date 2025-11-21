from tp2.util import StaticArray, alloc
from dataclasses import dataclass

@dataclass
class ArrayList:
    taille_max: int
    tab: StaticArray = alloc(taille_max)
    fin: int

def al_new(m:int=10, l:list[int] | None = None) -> ArrayList:
    assert m >= len(l)
    liste = ArrayList(m, l, len(l)-1)
