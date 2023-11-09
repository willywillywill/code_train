"""
https://steam.oxxostudio.tw/category/python/zerojudge/a410.html
ax+by=c
dx+ey=f

x = (c*e-f*b)/(a*e-d*b)
"""

a,b,c,d,e,f = list(map(int,input().split()))

if (a*e-d*b) != 0:
    x = (c*e-f*b)/(a*e-d*b)
    y = (a*f-d*c)/(a*e-d*b)
    print("x=%.2f"%(x))
    print("y=%.2f"%(y))
else:
    if (a*e-d*b)==(a*f-d*c)==0:
        print("Too many")
    else:
        print("No answer")
