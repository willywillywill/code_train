lst = input().split("],[")
lst = [ list(map(int,i.replace("[","").replace("]","").split(",")))
         for i in lst ]
arr = []
txt = list("零壹貳參肆伍陸柒捌玖")

for i in range(1,len(lst)):
    if max(lst[i-1]) >= min(lst[i]):
        out = []
        
        for j in [min(min(lst[i-1]),min(lst[i])),
                  max(max(lst[i-1]),max(lst[i]))]:
            o = ""
            for k in str(j):
                o += txt[int(k)]
            out.append(o)
        arr.append(out)
    else:
        out = []
        for j in lst[i]:
            o = ""
            for k in str(j):
                o += txt[int(k)]
            out.append(o)
        arr.append(out)

        
print(str(arr)[1:-1])


"""
[2,3],[3,6],[8,11],[13,17]
[800,900],[700,999] 
"""
