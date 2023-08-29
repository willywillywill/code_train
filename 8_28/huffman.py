class node:
    def __init__(self, id,ch,w,t,le,ri):
        self.id = id
        self.ch = ch
        self.w = w
        self.t = t
        self.le = le
        self.ri = ri

def dfs(id, level):
    if hf[id].t == False:
        code[level] = "0"
        dfs(hf[id].le, level+1)
        code[level] = "1"
        dfs(hf[id].ri, level+1)
    else:
        print(hf[id].ch," ", end=" ")
        for i in range(level):
            print(code[i], end="")
        print()

hf = [0]*101
code = [0]*10

c = ["a","b","c","d","e"]
w = [10,4,5,7,8]
num = len(c)
tmp = []
for i in range(num):
    hf[i] = node(i, c[i], w[i], True, 0,0)
    tmp.append(hf[i])

tmp = sorted(tmp, key=lambda x:x.w)

while len(tmp) > 1:
    a = tmp.pop(0)
    b = tmp.pop(0)
    n = node(num, None, a.w+b.w, 0, a.id, b.id)
    hf[num] = n
    tmp.append(n)
    tmp = sorted(tmp, key=lambda x:x.w)
    num += 1

dfs(tmp[0].id, 0)