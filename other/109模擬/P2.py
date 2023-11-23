roma = {
    1000:"M",900:"CM",500:"D",400:"CD",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"
}
for _ in range(int(input())):
    n = int(input())
    ans = ""
    while n:
        for i in roma:
            if n>=i:
                k = n//i
                n -= k*i
                ans += k*roma[i]
    print(ans)
