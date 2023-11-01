dit = {
    "{":[],
    "}":[],
    "[":[],
    "]":[],
    "(":[],
    ")":[],
}
s = input()

for i in range(len(s)):
    dit[s[i]].append(i)
lst = list(dit.values())

for i in range(0,6,2):
    if len(lst[i]) != len(lst[i+1]):
        print(0)
        break
else:
    tf = False
    for a,b in [("(",")"),("{","}"),("[","]")]:
        lst = [ (dit[a][i],dit[b][i]) for i in range(len(dit[a])) ]
        for c,d in lst:
            if c>d:
                print(0)
                tf = True
                break
        if tf:
            break
    else:
        print(1)

"""
{{[[((]]))}}
][][][
{}[]
(()
"""