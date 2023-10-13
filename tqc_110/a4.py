dit={}
for i in input().lower():
    if i not in [" ","."]:
        dit[i] = dit.get(i,0)+1
k = list(dit.items())
k.sort(key=lambda x:(x[1],-ord(x[0])),reverse=True)

print(sum([i[1] for i in k[:5] ]))
print("".join([i[0] for i in k[:5] ]))
"""
Failure is the mother of success.
While there is life there is hope.
"""