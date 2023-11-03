"""
Manacher O(n) 

最長回文子字串
偶回文
奇回文


"""


s = list(input())
le = len(s)
lst = "$#"+"#".join(s)+"#@"
p = [0]*len(lst)
mx = 0
di = 0

for i in range(1,le*2+2):
    if mx > i:
        p[i] = min(mx-i, p[di*2-i])
    else:
        p[i] = 1
    
    while lst[i-p[i]] == lst[i+p[i]]:
        p[i]+=1
    if p[i]+i > mx:
        mx = p[i]+i
        di = i
print(p)
print(max(p)-1)