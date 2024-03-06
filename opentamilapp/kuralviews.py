# (C) 2024, Ezhil Language Foundation
from kural import Kural
from kuralgen import get_matching_kural
from functools import lru_cache

class KuralWrapper:
    @property
    def row1(self):
        return self.ta.split('\n')[0]

    @property
    def row2(self):
        return self.ta.split('\n')[1]

Kural.row1 = KuralWrapper.row1
Kural.row2 = KuralWrapper.row2

@lru_cache(maxsize=1)
def kurals():
    data = Kural.load_data_base()
    assert len(data) == 1330
    return data

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
        d[a.adhikaram+' '+a.pal] = d.get(a.adhikaram+'_'+a.pal, list())
    for a in kurals():
        d[a.adhikaram+' '+a.pal].append(a)
    l1 = sum(map(len,d.values()))
    l2 = len(kurals())
    assert l1 == l2
    return d
