f = lambda a,b,m: (a+b)%m == (a-b)%m

for _ in range(int(input())):
    in1 = list(map(int, input().split()))
    a_min,a_max,b_min,b_max,c_min,c_max = in1
    
    n=0
    for i in range(a_min,a_max+1):
        for j in range(b_min,b_max+1):
            for k in range(c_min,c_max+1):
                if f(i,j,k):
                    n+=1
    print(n)
    

"""
4
1 2 2 4 3 4
1 2 2 4 6 7
3 4 2 4 6 7
5 9 10 12 2 9 

5
1 1 1 1 1 1
1 2 1 2 1 2
1 5 1 5 1 2
1 5 1 5 3 4
1 5 1 5 1 4
"""