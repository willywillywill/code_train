in1 = input()
in2 = input()
dit = {"A":0,"B":0}

m = []
for i in in2:
    if i in m:
        print("0A0B")
        break
    m.append(i)
    if i.isalpha():
        print("0A0B")
        break
else:
    if len(m)!= 4:
        print("0A0B")
    else:
        for i in range(len(in1)):
            if in1[i] == in2[i]:
                dit["A"] += 1
            elif in2[i] in in1 and in1[i] != in2[i]:
                dit["B"] += 1

        print("%dA%dB"%(dit["A"],dit["B"]))