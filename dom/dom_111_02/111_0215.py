now_x = 0
now_y = 0

move = {
    "U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)
}
for i in input():
    now_x += move[i][0]
    now_y += move[i][1]
if now_x==now_y==0:
    print("Y")
else:
    print("N")