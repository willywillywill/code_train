dit = {
    "T":0,"a":0,"i":0,"p":0,"e":0,"i":0
}

in1 = input()

for i in in1:
    if i in dit:
        dit[i] += 1
print(min(dit.values()))