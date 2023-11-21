
for _ in range(int(input())):
    in1 = input()
    st = set()
    for i in in1:
        if i.isdigit():
            st.add(i)
    lst = sorted(list(st), key=lambda x: int(x))
    if lst:
        print("".join(lst))
    else:
        print("N")
"""
2
0909ab2cckd7
ab21cdgcbgq123
"""