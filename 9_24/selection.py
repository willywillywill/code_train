lst = [0,5,7,2,4,8,4]
lst_s = []

while lst:
    k = lst.pop(lst.index(min(lst)))
    lst_s.append(k)
print(lst_s)