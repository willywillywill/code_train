t = [500.5]

for i in range(1,int(input())):
    t.append(t[i-1]+i* 3.14159)
print(t[-1])