a,b = list(map(int,input().split()))
out = []
for i in range(a,b+1):
    s = str(i)
    l = [ int(ii)**len(s) for ii in s ]
    if sum(l)==i:
        out.append(str(i))
if out:
    print(" ".join(out))
else:
    print("none")