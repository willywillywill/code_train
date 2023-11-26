lst = []
for _ in range(int(input())):
    a,b,c = input().split()
    if b=="*":
        lst.append((int(a)*int(c))**2)
    elif b=="+":
        lst.append((int(a)+int(c))-lst[-1])
    elif b=="-":
        lst.append(lst[-1]*(int(a)-int(c)))
    elif b=="/":
        a = int(a)
        if a%2==0:
            a //= 2
        else:
            a = (a+1)//2
        lst.append(a)

for i in lst:
    print(i)

"""
5
4 * 5
2 + 5
3 - 1
20 / 3
13 / 24
"""