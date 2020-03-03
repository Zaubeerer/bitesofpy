from collections import namedtuple
from datetime import datetime
import json
from typing import NamedTuple

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    nt_subclass = namedtuple("blog", dict_.keys())
    return nt_subclass(**dict_)
    

def nt2json(nt: NamedTuple):
    json.dumps(nt._asdict())