# lose ???

F = {
    "N":(0,1),
    "E":(1,0),
    "S":(0,-1),
    "W":(-1,0),
} # x,y
NESW = list("NESW")
LR = {
    "L":-1,
    "R":1
}

max_x,max_y = list(map(int,input().split()))
lose = {}

while 1:
    try:
        x,y,nesw = input().split()
        x,y = int(x),int(y)
        for i in input():
            if i in LR:
                nesw = NESW[(LR[i]+NESW.index(nesw))%4]
            else:
                if "%s,%s"%(x,y) in lose:
                    
                    continue
                x += F[nesw][0]
                y += F[nesw][1]
            if (x>=max_x or y>=max_y):
                lose["%s,%s"%(x,y)] = [nesw,"F"]
                print(x,y,nesw, "LOSE")
                break
        else:
            print(x,y,nesw)
    except:
        break

"""
5 3
0 3 W
LLFFFLFLFL
"""