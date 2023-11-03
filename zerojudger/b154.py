for _ in range(int(input())):
    lst = list(map(int,input().split()))
    l1 = lst[:3]
    l2 = lst[3:]

    k0 = [l1[0],l2[0]]
    k1 = [l1[1],l2[1]]

    l3 = [ l1[i]*k0[1]-l2[i]*k0[0] for i in range(len(l1)) ]
    l4 = [ l1[i]*k1[1]-l2[i]*k1[0] for i in range(len(l1)) ]

    for i in range(len(l3)-1):
        if l3[i] != 0:
            print(l3[2]//l3[i], end=" ")
        if l4[i] != 0:
            print(l4[2]//l4[i], end=" ")
    print()



"""
2
0 2 20 1 0 10
2 5 2 1 2 7
"""