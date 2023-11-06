for _ in range(int(input())):
    lst = input().split("}, {")
    lst = [  set(int(j) for j in i.replace("}","").replace("{","").split(",")) 
                for i in lst ]

    A = lst[0].copy()
    B = lst[1].copy()

    a1 = str(sorted(A|B)).replace("[","{").replace("]","}") if A|B else "N"
    a2 = str(sorted(A&B)).replace("[","{").replace("]","}") if A&B else "N"
    a3 = str(sorted(A-B)).replace("[","{").replace("]","}") if A-B else "N"
    a4 = str(sorted(A^B)).replace("[","{").replace("]","}") if A^B else "N"
    print("%s, %s, %s, %s"%(a1,a2,a3,a4))


"""
3
{1, 3}, {2, 4}
{1, 2, 3}, {3, 4, 5}
{1, 2}, {2, 1}
"""