import sys

for _ in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    f = 0
    for i in range(2,n+1):
        f = (f+m)%i
    print("Case %d:"%(_+1),f+1)
