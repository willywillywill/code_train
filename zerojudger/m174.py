
for _ in range(int(input())):
    lst = input().replace("[","").replace("]","").split(",")
    if lst == [""]:
        print(0)
        continue
    lst = list(map(int,lst))
    st1 = set(range(len(lst)+1))
    st2 = lst

    ans = set()
    while st2:
        u = st2.pop(0)
        if u in st1:
            ans.add(u)

    print(max(st1-ans))