import itertools

n = input()
if list(n).count("0") > 1:
    print(0)
else:
    ans = 0
    lst = list(itertools.combinations(n,len(n)-2))
    for i in lst:
        m = int("".join(i))
        if m%7==0 and m%3==0:
            ans = 1
    print(ans)