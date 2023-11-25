n = int(input())
lst = [1]
idx = 0
while len(lst) < 1000:
    lst.append(lst[idx]*2+1)
    lst.append(lst[idx]*3+1)
    idx += 1
lst.sort()
ans = set()
for i in range(len(lst)):
    if (lst[i]*2+1 in lst) and (lst[i]*3+1 in lst):
        ans.add(lst[i])
    if len(ans)==n:
        break
for i in sorted(list(ans)):
    print(i)