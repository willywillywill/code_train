txt = list("AEIOUaeiou")
in1 = list(map(str,input().lower()))
for i in range(len(in1)):
    if in1[i] in txt:
        in1[i] = in1[i].upper()
        break
for i in range(len(in1)-1,-1,-1):
    if in1[i] in txt:
        in1[i] = in1[i].upper()
        break
print("".join(in1))