# (C) 2024, Ezhil Language Foundation
from kural import Kural
from kuralgen import get_matching_kural
from anicham import yappu_venba,EerasaiType,MoovasaiType,Venba,EetruSeerAsai
from functools import lru_cache
from tamil.utf8 import is_tamil_unicode, get_letters

def ta_correct(text):
    correct_text = ''.join(map(lambda x: is_tamil_unicode(x) and x or ' ',get_letters(text)))
    return correct_text

class KuralWrapper:
    @property
    @lru_cache(maxsize=1)
    def row1(self):
        return ta_correct(self.ta.split('\n')[0])

    @property
    @lru_cache(maxsize=1)
    def row2(self):
        return ta_correct(self.ta.split('\n')[1])

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

def சீர்_பிரித்த_குறள்(எண்):
    def to_letters(அசை):
        if not அசை: return []
        result = []
        for key, _val in அசை.__dict__.items():
            if hasattr(_val, 'ezhutthu_list'):
                result.append(''.join([x.letter for x in _val.ezhutthu_list]))
        return result

    def to_seer(seer_list: List[Seer]):
        objs = []
        for seer in seer_list:
            if not seer: continue
            for key, _val in seer.__dict__.items():
                objs.append("-".join(to_letters(_val)))
        return list(filter(lambda x: x, objs))

    குறள் = kural.Thirukkural().get_kural_no(எண்)
    பகுப்பாய்வு: Venba = yappu_venba(குறள்.ta)
    return (' '.join(to_seer(பகுப்பாய்வு.adi_list[0].seer_list)),
            ' '.join(to_seer(பகுப்பாய்வு.eetradi.seer_list)))
