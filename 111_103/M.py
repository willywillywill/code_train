# !!!


import itertools

n = int(input())
k = list(itertools.product([1,0],repeat=n))
k.sort(key=lambda x:(x[0]))
