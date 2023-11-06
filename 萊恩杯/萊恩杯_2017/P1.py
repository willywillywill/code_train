import itertools

def chick(x):
    a1 = x[0].isdigit()
    a2 = x[2].isdigit()
    a3 = x[4].isdigit()

    return a1==a2==a3==True


out = []
txt = list("+-*/")
n = list(map(int,input().split()))
for i in list(itertools.permutations(n+txt,5)):
    i = "".join([ str(j) for j in i ])
    if chick(i) and eval(i)==16:
        out.append(i)
if out:
    print(out[-1])
else:
    print("None")