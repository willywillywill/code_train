k = int(input())

def f(i):
    if i!=1:
        f(i-1)
    n = i*2
    print(" "*(k-i)+ "*"*((n-1)//2)+"*"+"*"*((n-1)//2))
f(k)


"""
in 7
1
13
"""