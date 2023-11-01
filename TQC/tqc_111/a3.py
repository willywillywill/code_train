lst = list(map(float,input().split()))
c = lst[0]/lst[2]

def f(i):
    if i==0:
        return 0
    return (lst[0]-(c*(i-1)))*((lst[1]/100)/12)+f(i-1)

print(f(lst[2]))

"""
36000 12 9
8700000 2.4 15
"""