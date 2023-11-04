m1 = list(map(int,input().split()))
o1 = list(map(int,input().split()))
m2 = list(map(int,input().split()))
o2 = list(map(int,input().split()))
wm = 0
wo = 0
mo = 0
if sum(m1)>sum(o1):
    wm +=1
elif sum(m1)<sum(o1):
    wo += 1
else:
    mo += 1
if sum(m2)>sum(o2):
    wm +=1
elif sum(m2)<sum(o2):
    wo += 1
else:
    mo += 1

print("%d:%d"%(sum(m1),sum(o1)))
print("%d:%d"%(sum(m2),sum(o2)))
if wm==2:
    print("Win")
elif wo==2:
    print("Lose")
else:
    print("Tie")