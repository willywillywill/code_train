# 單位價格 val / time
lst = list(map(int,"15,2,0,1,5,2,1,3,0,1,1".split(",")))
sum_t = lst[0]
max_num = lst[1:]
val = [2,40,300,200,100,90,20,50,60,5]
time = [1,4,24,15,7,7,3,5,5,2]
vt = [ val[i]/time[i] for i in range(len(val)) ]
vt = [ [vt[i],time[i],val[i],max_num[i]] for i in range(len(val)) ]
vt.sort(key=lambda x:x[0],reverse=True)
print(vt)
count = 0
while vt:
    _,dtime,dval,dnum = vt.pop(0)
    while dnum and sum_t>=dtime:
        dnum -= 1
        sum_t -= dtime
        count += dval
print(count)

"""
10,1,1,0,1,0,1,1,1,0,1
15,2,0,1,5,2,1,3,0,1,1
"""