# ~ b159

for _ in range(int(input())):
    x = list(map(int, input().split()))
    card = [ 0 for i in range(53) ]
    card_num = [0 for i in range(15)]
    card_type = [0,0,0,0]
    for a in x:
        card[a] = 1
        card_num[(a-1)%13+1] += 1
        if (a-1)%13+1 == 1:
            card_num[14] += 1
        card_type[int((a-1)/13)] += 1
   
    point = []
    cnt = 0
    max_cnt = 0
    start = -1
    for a in range(1,15):
        if card_num[a]>0:
            cnt += 1
            if cnt == 1:
                start = a
            if max_cnt < cnt:
                max_cnt = cnt
            continue
        cnt = 0
    if max_cnt >= 5:
        flag = True
        type1 = 0
        for i in range(1,4):
            if card_type[type1] < card_type[a]:
                type1 = a
        start += type1*13

        for a in range(start,start+5):
            if ((a-1)%13+1)==1:
                a -= 13
            if card[a] == 0:
                flag = False
                break
        if flag:
            point.append(7)
        else:
            point.append(4)
    g1 = 0
    g2 = 0
    for a in range(1,14):
        if g1==0 and card_num[a] >= 2:
            g1 = card_num[a]
            continue
        if g1 !=0 and card_num[a] >= 2:
            g2 = card_num[a]
    if g1==4 or g2==4:
        point.append(6)
    elif (g1==3 and g2>=2) or (g1==3 and g2>=2):
        point.append(5)
    elif g1==3:
        point.append(3)
    elif g1==2 and g2>=2 or g2==2 and g1>=3:
        point.append(2)
    elif g1==2:
        point.append(1)
    else:
        point.append(0)

    print(max(point))
"""
2 
3 44 4 6 7 5 
19 12 1 32 45 25

2 
14 16 18 19 20 21 
4 17 30 43 9 22
"""