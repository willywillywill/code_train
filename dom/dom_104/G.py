# !!
# string

for _ in range(int(input())):
    n = list(map(int, input().split(",")))
    A = []
    B = []
    AB = []
    xy = {}
    for i in range(n[0]):
        k = list(map(str, input().split()))
        if 9999 in k:
            xy["A"] = [i,k.index(9999)]
        A.append(k)
    for i in range(n[2]):
        k = list(map(str, input().split()))
        if 9999 in k:
            xy["B"] = [i,k.index(9999)]
        B.append(k)

    for i in range(n[0]):
        k = list(map(str, input().split()))
        if 9999 in k:
            xy["AB"] = [i,k.index(9999)]
        AB.append(k)

    ans = {}

    for i in range(len(A)):
        for j in range(len(B[0])):
            A_ = A[i][::]
            B_ = [ B[k][j] for k in range(len(B))]
            if "9999" in A_ or "9999" in B_:
                ans[AB[i][j]] = [ A_[i]+" "+B_[i] for i in range(len(A_)) ] 

    ans_ = []
    for i in ans:
        j=0
        ok = True
        while ok:
            k = list(map(int, ans[i][j].split()))
            if 9999 in k and 0 in k:
                ok = False
            if j > len(ans[i])-2:
                break
            else:
                j+=1
        if ok:
            ans_.append([i]+ans[i])


    ans_ = ans_[0]
    c = int(ans_.pop(0))
    s = 0
    for i in ans_:
        k = list(map(int,i.split()))
        if 9999 in k:
            b = k[1] if k[0]==9999 else k[0]
        else:
            s+= k[0]*k[1]

    s = c-s
    print(int(s/b))