

flag = False
move = [ (2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1) ]
m = [ [0]*8 for _ in range(8) ]
s,f = input().split()
m[ord(f[0])-97][int(f[1])-1] = 3  # f




for i in m:
    print(*i)