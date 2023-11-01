while 1:
    try:
        in1 = list(input())
        in2 = list(input())
        in1,in2 = [in1,in2] if len(in1) > len(in2) else [in2,in1]
        ans = []
        while in2:
            s = in2.pop(0)
            if s in in1:
                ans.append(in1.pop(in1.index(s)))
        ans.sort()
        print("".join(ans))
    except:
        break

"""
inging
singing
abc

efg

ghi
a
a
"""