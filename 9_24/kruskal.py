# minimum cost spanning tree

class edge:
    def __init__(self) -> None:
        self.start = 0
        self.to = 0
        self.find = 0
        self.val = 0
        self.next = 0



def findmincost(head):  # search min edge
    minval = 100
    ptr = head
    while ptr != None:
        if ptr.val < minval and ptr.find==0:
            minval = ptr.val
            retptr = ptr
        ptr=ptr.next
    retptr.find = 1
    return retptr

def mintree(head): # construction tree
    global VERTS
    result = 0
    ptr=head
    for i in range(VERTS):
        v[i] = 0
    while ptr != None:  # !!!
        mceptr = findmincost(head)
        v[mceptr.start] = v[mceptr.start]+1
        v[mceptr.to] = v[mceptr.to]+1
        print(mceptr.start, mceptr.to, v[mceptr.start], v[mceptr.to])
        if v[mceptr.start] > 1 and v[mceptr.to] > 1:
            v[mceptr.start] = v[mceptr.start]-1
            v[mceptr.to] = v[mceptr.to]-1
            result=1
        else:
            result=0
        if result==0:
            print("start spot %d -> end spot %d -> distance %d"%(mceptr.start, mceptr.to, mceptr.val))
        ptr = ptr.next

data = [
    [1,2,6],[1,6,12],[1,5,10],[2,3,3],\
    [2,4,5],[2,6,8],[3,4,7],[4,6,11],\
    [4,5,9],[5,6,16]
]
VERTS = 6
v = [0]*(VERTS+1)

head = None

for i in range(len(data)):
    for j in range(1, VERTS+1):
        if data[i][0]==j:
            newnode = edge()
            newnode.start = data[i][0]
            newnode.to = data[i][1]
            newnode.val = data[i][2]
            newnode.find = 0 
            newnode.next = None
            if head == None:
                head = newnode
                ptr = head
            else:
                ptr.next = newnode
                ptr = ptr.next

mintree(head)
print(v)