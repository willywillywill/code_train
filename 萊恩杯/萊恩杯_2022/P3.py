def c(x):
    x.sort()
    for i in range(1,len(x)):
        if x[i-1]+1 != x[i]:
            return False
    return True
def c2(x):
    x.sort()
    k = 0
    if 1 in x:
        for i in range(1,len(x)):
            if x[i-1]+1 != x[i]:
                k = 1
    if 14 in x:
        for i in range(1,len(x)):
            if x[i-1]+1 != x[i]:
                k = 1
    return bool(k)

type2_txt = ["梅花","方塊","紅心","黑桃"]
dit = {1:"A",11:"J",12:"Q",13:"K"}
for i in range(2,11):
    dit[i] = str(i)

in1 = list(map(int,input().split()))
type1 = [ i%13 if i%13 else 13 for i in in1 ]
type2 = [ (i-1)//13 for i in in1 ]

type3 = ""

if type2[0] == type2[-1]:
    if (1 in type1 or 14 in type1) and c2(type1.copy()):
        type3 = "同花順子"
    else:
        type3 = "同花"
elif [ i for i in set(type1) if type1.count(i)>=4 ]:
    type3 = "鐵支"
elif [ i for i in set(type1) if type1.count(i)==3 ] and \
    [ i for i in set(type1) if type1.count(i)==2 ]:
    type3 = "葫蘆"
elif type2[0] == type2[-1]:
    type3 = "同花"
elif c(type1.copy()):
    type3 = "順子"
elif [ i for i in set(type1) if type1.count(i)==3 ]:
    type3 = "三條"
elif len([ i for i in set(type1) if type1.count(i)==2 ])==2:
    type3 = "兩對"
elif [ i for i in set(type1) if type1.count(i)==2 ]:
    type3 = "一對"
else:
    type3 = "無"


for i in range(5):
    print(type2_txt[type2[i]],dit[type1[i]],end=" ")
print(type3)


"""
27 37 39 38 36
14 48 9 28 1 
"""