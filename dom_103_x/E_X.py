# ~ b159
import itertools

for _ in range(int(input())):
    inp = list(map(int,input().split()))
    inp = itertools.combinations(inp,5)
    out = 0
    for in1 in inp:
        ans = [0]
        in1 = sorted(list(in1))
        mod_lst = [ (ii-1)%13+1 for ii in in1 ]
        div_lst = [ (ii-1)//13+1 for ii in in1 ]

        times = { i:mod_lst.count(i) for i in mod_lst } 
        if 4 in times.values(): # 四條
            ans.append(6)
        elif 2 in times.values() and 3 in times.values(): # 葫蘆
            ans.append(5)
        elif 3 in times.values(): # 三條
            ans.append(3)
        elif list(times.values()).count(2)==2: # 兩對
            ans.append(2)
        elif 2 in times.values(): # 一對
            ans.append(1)
        
        for i in range(1,len(in1)): # 順子
            times_1 = 1
            for j in range(i,len(in1)):
                if in1[j-1]+1 != in1[j]:
                    break
                else:
                    times_1 += 1
            if times_1==5:
                ans.append(4)
        
            times_2 = 1
            for j in range(i,len(in1)):
                if in1[j-1]+1 != in1[j] or div_lst[j-1] != div_lst[j]:
                    break
                else:
                    times_2 += 1
            if times_2==5:
                ans.append(7)

        out = max(max(ans),out)
    print(out)
    


"""
2 
3 44 4 6 7 5 
19 12 1 32 45 25 

2 
14 16 18 19 20 21 
4 17 30 43 9 22
"""