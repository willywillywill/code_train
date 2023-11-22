class node:
    def __init__(self, v) -> None:
        self.val = v
        self.left = None
        self.right = None
def build(inOrder, preOrder):
    if inOrder:
        idx = inOrder.index(preOrder.pop(0))
        root = node(inOrder[idx])
        root.left = build(inOrder[:idx], preOrder)
        root.right = build(inOrder[idx+1:], preOrder)
        return root
def postOrder(root, l):
    if root:
        postOrder(root.left, l)
        postOrder(root.right, l)
        l.append(str(root.val))

while 1:
    try:
        preOrder, inOrder = map(list,input().split())
        root = build(inOrder, preOrder)
        ans = []
        postOrder(root, ans)
        print("".join(ans))
    except:
        break