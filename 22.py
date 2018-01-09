import pprint

d = {}
a = list(range(1,11))
b = list(range(11,21))
c = list(range(21,31))
d["a"] = a
d["b"] = b
d["c"] = c
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)

'''
from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

pprint(d)
'''
