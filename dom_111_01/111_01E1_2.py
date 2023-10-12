while 1:
    try:
        dic={}
        f=False; Tree=True #f判斷是否中斷讀取, Tree判斷是不是樹
        while 1:
            s=input().split()
            for i in s:
                if i=='()': #讀到這個才中斷讀取
                    f=True
                else:
                    a,b=i[1:len(i)-1].split(',')
                    if b=='':
                        b='root'
                    if b in dic:
                        Tree=False #有重複節點
                    dic[b]=a
            if f:
                break

        if 'root' not in dic:
            Tree=False #沒有根節點
        if Tree:
            tree=[]
            tree.append(dic['root'])
            del dic['root']
            q=['L','R']
            while q:
                node=q.pop(0)
                if node in dic:
                    tree.append(dic[node])
                    q.append(node+'L')
                    q.append(node+'R')
                    del dic[node]

        if len(dic)>0:
            print('not complete')
        elif not Tree:
            print('not complete')
        else:
            print(*tree)
    except:
        break

"""
(11,LL) (7,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(3,L) (4,R) ()
(11,LL) (7,LLL) (2,LLL) (8,R) (5,) (4,L) (13,RL) (2,LLR) (1,RRR) (4,RR) ()
(5,) (3,) (4,R) ()
(5,) (3,LL) ()
(5,) ()
"""