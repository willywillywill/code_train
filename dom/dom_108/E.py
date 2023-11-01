for _ in range(int(input())):
    in1 = list(map(int,input().split()))
    in2 = []
    for i in range(in1[0]):
        in2.append(list(input().strip()))

    for i in range(in1[1]):
        k = [in2[ii][i] for ii in range(in1[0])]
        dit = {}
        for j in k:
            dit[j] = dit.get(j,0)+1

        d = list(dit.items())
        d.sort(key=lambda x:x[1], reverse=True)
        v = set([ i[1] for i in d ])
        w = [ i[0] for i in d ]
        if len(v) == 1:
            for j in list("ACGT"):
                if j in w:
                    print(j, end="")
                    break
        else:
            print(d[0][0],end="")
            
    print()
"""
2
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TGAGATAC 
4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA

2
6 10
ATGTTACCAT
AAGTTACGAT
AACAAAGCAA
AAGTTACCTT
AAGTTACCAA
TACTTACCAA
4 9
GAGCACGTC
CATCACGTG
GCTTACGTT
CCGTATGTA 

TAAGATAC
ACGTACGTAA

AAGTTACCAA
CAGCACGTA
"""