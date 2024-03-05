# (C) 2024, Ezhil Language Foundation
from kural import Kural
from kuralgen import get_matching_kural
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
    assert len(d.keys()) == 3
    return d

@lru_cache(maxsize=1)
def get_adhikaram():
    d={}
    for a in kurals():
        d[a.adhikaram] = d.get(a.adhikaram, list())
    for a in kurals():
        d[a.adhikaram].append(a)
    l1 = sum(map(len,d.values()))
    l2 = len(kurals())
    assert l1 == l2
    return d
