


dit = {}
s = input().split()
for i in s:
    i = i.lower()
    dit[i] = dit.get(i,0)+1
dit = list(dit.items())
dit.sort(key=lambda n:n[1], reverse=True)

if dit[0][1] != dit[1][1]:
    print(dit[0][0], dit[0][1])
else:
    print("No")

