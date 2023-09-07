for _ in range(int(input())):
    str_a = list(input())
    str_b = list(input())

    b = str_b if len(str_a) < len(str_b) else str_a
    s = str_b if len(str_a) > len(str_b) else str_a
    lst = []
    while s:
        ss = s.pop(0)
        if ss in b:
            lst.append(b.pop(b.index(ss)))
    
    lst = sorted(list(set(lst))) if lst else "N"
    print("".join(lst))

"""
3
download
women
banana
naan
then
street 
"""