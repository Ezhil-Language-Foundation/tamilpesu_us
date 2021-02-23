import random
from pprint import pprint


def get_n_unique(n, r_range):
    rval = []
    assert n < len(r_range)
    while n > 0:
        rval.append(random.choice(r_range))
        n -= 1
        del r_range[r_range.index(rval[-1])]
    return rval


pprint(get_n_unique(5, list(range(0, 10))))

pprint(get_n_unique(2, list(range(0, 3))))

pprint(get_n_unique(2, list(range(0, 3))))

pprint(get_n_unique(2, list(range(0, 3))))
