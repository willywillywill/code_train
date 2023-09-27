class node:
    def __init__(self, data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data

def buildTree(preorder,inorder):
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
        res.append(root.data)

while 1:
    try:
        preorder,inorder = list(map(list,input().split()))
        root = buildTree(preorder, inorder)
        res = []
        postorder(root)
        print("".join(res))
    except:
        break

"""
DBACEGF ABCDEFG
"""