s = list(input())

a = 0
b = 0
c = 0
v = [0]*len(s)
for i in range((len(s))):
    if v[i]:
        continue

    if s[i]=="C":
        if i+1 == len(s):
            a += 1
            v[i] = 1
        elif s[i+1]=="#":
            c += 1
            v[i],v[i+1]=1,1
        elif s[i+1]=="+":
            b += 1
            v[i],v[i+1],v[i+2] = 1,1,1
        else:
            a+=1
            v[i] = 1
print("{},{},{}".format(a,b,c))