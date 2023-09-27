# !!!!

"""
4
5,8 5,3 5,2 5,4 5,6 1,2 2,0
8,1 1,3 6,2 8,10 7,5 1,4 7,8 8,6 8,0
3,8 6,8 6,4 0,6 8,2 2,0 5,3
1,0 4,3 1,2 

5
1,2 2,3 4,0
4,3 2,3 2,1 1,0
1,2 2,3 3,4 1,4 1,5
1,2 1,3 2,3
1,2 2,3 3,4 1,5 5,4 

"""
class edge:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        self.f = False

in1 = list(map(str, "5,8 5,3 5,2 5,4 5,6 1,2 2,0".split(" ")))
in1 = [ list(map(int, i.split(","))) for i in in1 ]
in1 = [ edge(i[0],i[1]) for i in in1 ]

        
