
class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def buildTree(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = node(inorder[idx])
        root.left = buildTree(preorder, inorder[:idx])
        root.right = buildTree(preorder, inorder[idx+1:])
        return root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        res.append(str(root.data))
for _ in range(int(input())):
    in_lst = list(map(int, input().split(",")))
    pre_lst = list(map(int, input().split(",")))
    res = []

    root = buildTree(pre_lst, in_lst)
    postorder(root)
    print(",".join(res))