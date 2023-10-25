


in1 = list(map(int,input().split()))
in1.sort()
mod_lst = [ (i-1)%13+1 for i in in1 ]
div_lst = [ (i-1)//13+1 for i in in1 ]
ans = [0]
for j in range(len(in1)): # 同花順
    times = 1
    for i in range(1,j):
        if in1[i-1]+1 != in1[i] or div_lst[i-1] != div_lst[i]:
            break
        else:
            times += 1
    if times == 5:
        ans.append(7)
for j in range(len(in1)): # 順子
    times = 1
    for i in range(1,j):
        if in1[i-1]+1 != in1[i]:
            break
        else:
            times += 1
    if times == 5:
        ans.append(4)
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
    
print(ans)
print(max(ans))


"""
3 44 4 6 7 5 
1 1 1 1 2 2
"""