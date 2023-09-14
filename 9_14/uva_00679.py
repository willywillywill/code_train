
def f(D, idx, remainder):
    if D == 0: return idx
    if remainder % 2==1:
        idx *= 2
        remainder = (remainder+1)//2
    else:
        idx = 2*idx+1
        remainder //= 2
    return f(D-1, idx,remainder)
import sys
for _ in range(int(input())):
    D, I = map(int,sys.stdin.readline().split())
    print(f(D-1, 1, I))
