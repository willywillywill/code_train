def c(lst):
    for i in range(1,len(lst)):
        if lst[i-1]+1 != lst[i]:
            return False
    return True

for _ in range(int(input())):
    in1 = list(map(int,input().split()))
    in1.sort()
    
    type1 = [ (i-1)//13+1 for i in in1 ]  # 花色
    type2 = [ (i-1)%13+1 for i in in1 ]   # 點數
    type2.sort()

    if (1 in type2) and type2==[1,10,11,12,13]:
        if min(type1) == max(type1):
            print('同花順')
        else:
            print('順子')
    elif c(type2):
        if type1[0]==type1[-1]:
            print('同花順')
        else:
            print('順子')
    else:
        dit = {}
        for i in set(tuple(type2)):
            if type2.count(i) not in dit:
                dit[type2.count(i)] = []
            dit[type2.count(i)].append(i)

        if 4 in dit:
            print('四條')
        elif (3 in dit and 2 in dit):
            print('葫蘆')
        elif 3 in dit:
            if 2 in dit:
                if len(dit[2]) == 2:
                    print('葫蘆')
            else:
                print('三條')
        elif 2 in dit:
            if len(dit[2]) == 2:
                print('兩對')
            else:
                print('一對')
        else:
            print('雜牌')

"""
3
3 44 4 19 7
6 12 1 32 45
26 25 2 38 39


1 2 3 4 5
10 11 12 13 14
"""