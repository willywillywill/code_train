def p(x):
    if x==2 or x==3:
        return True
    elif x>4:
        m = x%6
        if m != 1 and m!= 5:
            return False
        for i in range(5,int(x**0.5)+1,6):
            if x%i==0 or x%(i+2)==0:
                return False
        return True
    else:
        return False

import sys

try:
    for i in sys.stdin:
        a,b = list(map(int,i.split()))
        num = 0 
        for j in range(a,b+1):
            if p(j):
                num += 1
        print(num)
except:
    pass