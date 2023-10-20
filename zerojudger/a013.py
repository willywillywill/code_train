dit = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
def roman2int(s):
    s = [ dit[i] for i in s]
    i=1
    while len(s) > 1 and i<len(s):
        if s[i]>s[i-1]:
            s[i] = s[i]-s[i-1]
            del s[i-1]
        else:
            i+=1

    return sum(s)
p = [["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
def int2roman(num):
    r = ""
    for i in p:
        x = divmod(num,i[1])
        if x[0] != 0:
            r += i[0]*x[0]
            num = x[1]
    return r
    

while 1:
    in1 = input().split()
    if in1[0]=="#":
        break
    lst = list(map(roman2int,in1))
    d = abs(lst[0]-lst[1])
    print( int2roman(d) if d else "ZERO" )
