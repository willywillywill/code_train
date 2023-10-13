
def f_s(s:str):
    global stop_input,end,max_idx
    s = s.replace("(","")
    s = s.replace(")","")
    s = s.split(",")
    if s==[""]:
        stop_input=1
    else:
        n = 1
        for i in s[1]:
            n = n*2 if i=="L" else n*2+1
        if tree[n]:
            end = 1
        max_idx = max(max_idx,n)
        tree[n] = int(s[0])
while 1:
    try:
        stop_input = 0
        end = 0
        max_nodes_num = 10000000
        max_idx = 0
        tree = [0]*max_nodes_num
        while 1:
            in1 = list(map(f_s, input().split()))
            if stop_input:
                break
        if end or (not tree[1]):
            print("not complete")
            continue
        del tree[max_idx+1:]
        queue = [1]
        visited = [0]*len(tree)
        while queue:
            idx = queue.pop(0)
            if idx<len(tree):
                if tree[idx]:
                    visited[idx] = tree[idx]
                    queue.append(idx*2)
                    queue.append(idx*2+1)
        if visited == tree:
            out = [ i for i in visited if i ]
            print(*out)
        else:
            print("not complete")
    except:
        break

"""
(64,LLLRLLRRRL) (132,LLRL) (717,RRLRRLLRLRRL) (995,RRRRRRR) (345,RLRL) (42,LLLRLLRL) (219,RLLLRLRR) (843,RRLRRRLRRRL) (550,RRLRLLLL) (458,RRLLRLLRLRRLL) (320,RLRLLL) (918,RRRLLRLRL) (781,RRLRRLRRR) (743,RRLRRLLRRR) (569,RRLRLLLLRRR) (386,RRLLLRR) (427,RRLLRLLRLR) (856,RRLRRRRLR) (982,RRRRRLR) (917,RRRLLRL) (212,RLLLRLRRL) (366,RRLLLLR) (409,RRLLRLL) (485,RRLLRLLRLRRLLRR) (410,RRLLRLLRLL) (573,RRLRLLLLRRRR) (356,RRLLLLLR) (788,RRLRR) (727,RRLRRLLRLRR) (287,RLLRLRRRRR) (153,LRLR) (706,RRLRRLLRLRL) (241,RLLRLRLR) (802,RRLRRRLRLLL) (641,RRLR) (235,RLLRLRL) (282,RLLRLRRRR) (474,RRLLRLLRLRRLLR) (819,RRLRRRLRL) (510,RRLLRLLRLRRR) (304,RLLR) (620,RRLRL) (46,LLLRLLRLRL) (562,RRLRLLLLR) (500,RRLLRLLRLRR) (354,R) (15,LLL) (242,RLLRLR) (148,L) (36,LLLRLL) (350,RLRLR) (305,RLLRRL) (479,RRLLRLLRLRRLLRRL) (721,RRLRRLLRLRRLR) (712,RRLRRLLRLR) (191,) (587,RRLRLLLRR) (534,RRLLRLR) (109,LLLRLRL) (908,RRRLLLR) (684,RRLRRLLLR) (600,RRLRLLRLLRL) (117,LLLRRL) (223,RLLLRR) (962,RRRRLR) (154,LR) (998,RRRRRRRR) (262,RLLRLRRRRL) (384,RRLLLR) (978,RRRR) (933,RRRLLR) (57,LLLRLLR) (73,LLLRLLRRRLRL) (807,RRLRRRLRLLR) (804,RRLRRRLRLL) (344,RLRLLRR) (778,RRLRRLR) (874,RRLRRRRRL) (315,RLRLLLL) (160,LRR) (914,RRRLLRLL) (363,RRLLLLRL) (979,RRRRRL) (49,LLLRLLRLR) (116,LLLRRLL) (355,RRLLLLL) (126,LL) (739,RRLRRLLRRRL) (80,LLLRLLRRRLRRL) (418,RRLLRLLRLRLLR) (565,RRLRLLLLRR) (568,RRLRLLLLRRRL) (127,LLRLL) (203,RLLL) (523,RRLLRLLRRRR) (771,RRLRRLRLR) (937,RRRLRR) (834,RRLRRRLR) (419,RRLLRLLRLRL) (185,LRRRR) (76,LLLRLLRRRLR) (511,RRLLRLLR) (517,RRLLRLLRR) (613,RRLRLLRLR) (890,RRLRRRRRR) (693,RRLRRLL) (608,RRLRLLRL) (201,RLLLLR) (100,LLLRL) (832,RRLRRRLRLR) (255,RLLRLRRL) (920,RRRLLRLR) (775,RRLRRLRLRR) (258,RLLRLRR) (61,LLLRLLRR) (882,RRLRRRRRLRR) (397,RRLLLRRRR) (884,RRLRRRRR) (96,LLLRLLRRR) (379,RRLLL) (111,LLLRLR) (142,LLR) (325,RLRLL) (314,RL) (367,RRLLLLRR) (113,LLLR) (204,RLLLRL) (231,RLLRL) (393,RRLLLRRR) (876,RRLRRRRRLR) (753,RRLRRL) (831,RRLRRRLRLRL) (141,LLRLR) (487,RRLLRLLRLRRL) (548,RRLLRR) (260,RLLRLRRR) (29,LLLRLLL) (198,RLLLL) (632,RRLRLR) (17,LLLRLLLLL) (63,LLLRLLRRRLL) (417,RRLLRLLRLRLL) (848,RRLRRRLRRR) (416,RRLLRLLRL) (945,RRRRLL) (889,RRLRRRRRRLR) (798,RRLRRRL) (581,RRLRLLLR) (868,RRLRRRR) ()
"""