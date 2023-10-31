import bisect

l = [0]
while l[-1]+(1/(len(l)+1)) < 5.2:
    l.append(l[-1]+(1/(len(l)+1)))

while 1:
    try:
        print(bisect.bisect_left(l,float(input())),end=" card(s)\n")
    except:
        break