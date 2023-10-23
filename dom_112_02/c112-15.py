import  itertools

in1 = list(map(int,input().split(",")))
in1 = itertools.permutations(in1,3)
lst = set( sum(i) for i in list(in1) )
print(len(lst))
