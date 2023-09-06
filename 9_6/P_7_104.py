
in_s = list(map(str, "A,B,6 A,E,9 B,C,3 B,D,5 C,D,7 B,F,8 D,E,10 D,F,11 A,F,12 E,F,15".split()))
in_s = [ in_s[i].split(",")[:2]+[int(in_s[i].split(",")[2])] for i in range(len(in_s)) ]
in_s.sort(key=lambda x:x[2])
st = set()
for i in in_s:
    st.add(i[0])
    st.add(i[1])
dit = dict()
for i in list(st):
    dit[i] = i

def find_node(x):
    if dit[x] != x:
        dit[x] = find_node(dit[x])
    return dit[x]

mst = []
n = len(st)-1
for i in in_s:
    v1,v2,_ = i
    if find_node(v1) != find_node(v2):
        dit[find_node(v2)] = find_node(v1)
        mst.append(i)
        n-=1
        if n==0:
            break
num=0
for i in mst:
    _,_,c = i
    num+=c

print(num)

"""
A,B,6 A,E,9 B,C,3 B,D,5 C,D,7 B,F,8 D,E,10 D,F,11 A,F,12 E,F,15
"""