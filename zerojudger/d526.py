def insert_node(val,root):
    if root:
        if val > root["data"]:
            if root["right"]:
                insert_node(val, root["right"])
            else:
                root["right"] = {'data': val, 'left': None, 'right': None}
        else:
            if root["left"]:
                insert_node(val, root["left"])
            else:
                root["left"] = {'data': val, 'left': None, 'right': None}
    else:
        root = {'data': val, 'left': None, 'right': None}
    return root
def preOrder(root, l):
    if root:
        l.append(str(root["data"]))
        preOrder(root["left"], l)
        preOrder(root["right"], l)
    
while 1:
    try:
        input()
        lst = list(map(int,input().split()))
        root = None
        for i in lst:
            root = insert_node(i,root)
        ans = []
        preOrder(root,ans)
        print(" ".join(ans))
    except:
        break