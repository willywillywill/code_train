# OK

print("PERFECTION OUTPUT")
p = 1
while p:
    n = list(map(int, input().split()))
    for k in n:
        if k == 0:
            p = 0
            break
        print("%5d  "%(k), end="")
        l = [ j for j in range(1,k+1) if k%j==0 ]

        if sum(l[:-1]) == l[-1]:
            print("PERFECT")
        elif sum(l[:-1]) < l[-1]:
            print("DEFICIENT")
        elif sum(l[:-1]) > l[-1]:
            print("ABUNDANT")
print("END OF OUTPUT")
