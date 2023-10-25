dit = {}
while 1:
    try:
        a,b = list(map(str,input().split()))
        dit[b] = a
    except:
        break
print()
while 1:
    try:
        n = input()
        if n in dit:
            print(dit[n])
        else:
            print("eh")
    except:
        break

"""
dog ogday
cat atcay
pig igpay
froot ootfray
loops oopslay

atcay
ittenkay
oopslay
"""