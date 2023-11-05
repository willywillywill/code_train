
for _ in range(int(input())):
    in1 = [ i for i in input() if not i.isalpha() ]
    ans = ""
    s = ""
    while in1:
        k = in1.pop(0)
        if k in " +  -  *  /  %".split():
            if k=="/":
                ans += str(int(s))+"//"
            else:
                ans += str(int(s))+k
            s = ""
        else:
            s += k
    ans += str(int(s))
    print(eval(ans))

"""
5
Ab1cD34K+5Ol67i8
139v2Bk%14xHv7
Nb2y4W9/3UQg9
1k-L3
5p0i*2
"""