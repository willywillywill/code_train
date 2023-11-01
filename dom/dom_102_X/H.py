from itertools import combinations #組合

for _ in range(int(input())):
    ans=[]
    s=list(map(int, input().split()))
    
    score=[] #5張牌的分數
    suit=[] #花色--> 0黑桃 1紅心 2方塊 3梅花
    point=[] #牌的點數
    cnt=[] #計算每種點數共有幾張

    for i in s:
        suit.append((i-1)//13)
        point.append((i-1)%13 if i%13!=0 else 13) #點數13因為取餘數剛好會等於0, 所以+13
    
    for i in set(point): #計算點數的張數
        cnt.append(point.count(i))
    
    cnt.sort() #cnt要做排序, 因為[1, 4] != [4, 1]
   
    min_card=min(s) #5張牌中最小的點數
    point=sorted(point)
    if point==[1, 2, 3, 4, 5] or point==[1, 10, 11, 12, 13]: #先處理順子的特殊情況
        if len(set(suit))==1: #看所有牌是否為相同的花色
            print("同花順")
        else:
            print("順子")
    elif point==[i for i in range(min_card, min_card+5)]: #順子的一般情況
        if len(set(suit))==1:
            print("同花順")
        else:
            print("順子")
    elif cnt==[1, 4]: #四張相同的牌-->四條
        print("四條")
    elif cnt==[2, 3]: #三張相同的牌+兩張相同的牌-->葫蘆
        print("葫蘆")
    elif cnt==[1, 1, 3]: #三張相同的牌-->三條
        print("三條")

    elif cnt==[1, 2, 2]: #兩張相同的牌+兩張相同的牌-->二條
        print("二條")

    elif cnt==[1, 1, 1, 2]: #兩張相同的牌-->一條
        print("一條")
    else:
        print("雜牌")
