# (C) 2024, Ezhil Language Foundation
from kural import Kural
from functools import lru_cache

@lru_cache(maxsize=1)
def kurals():
    return Kural.load_data_base()

@lru_cache(maxsize=1)
def get_pals():
    d={}
    for a in kurals():
        d[a.pal] = d.get(a.pal,list())
        d[a.pal].append(a)
    return d

@lru_cache(maxsize=1)
def get_adhikaram():
    d={}
    for a in kurals():
        d[a.adhikaram] = d.get(a.adhikaram,list())
        d[a.adhikaram].append(a)
    return d
