dit = {}

while 1:
    try:
        en,ot = input().split()
        dit[ot] = en
    except:
        break
print()
while 1:
    try:
        ot = input()
        if ot in dit:
            print(dit[ot])
        else:
            print("eh")
    except:
        break
