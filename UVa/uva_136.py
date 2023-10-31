"""
out = 0
i = 1
while len(out) != 1500:
    n = i
    k = n
    while n%2==0:
        n //=2
    while n%3==0:
        n //=3
    while n%5==0:
        n //=5
else: 
    i+=1
print("The 1500'th ugly number is",*out,".")
"""


def nthUglyNumber(n):
    uglys=[1]
    u2=u3=u5=0
    while len(uglys)!=n:
        ugly=min(uglys[u2]*2,uglys[u3]*3,uglys[u5]*5)
        uglys.append(ugly)
        if uglys[u2]*2==ugly:
            u2+=1
        if uglys[u3]*3==ugly:
            u3+=1
        if uglys[u5]*5==ugly:
            u5+=1
    return uglys[n-1]
print(f"The 1500'th ugly number is {nthUglyNumber(1500)}.")