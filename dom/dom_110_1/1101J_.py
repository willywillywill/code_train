
class node:
    def __init__(self, val:int):
        self.val = val
        self.next = None
def build(n):
    head = node(1)
    pre = head
    for i in range(2,n+1):
        newNode = node(i)
        pre.next = newNode
        pre = newNode
    pre.next = head
    return head
while 1:
    try:
        n,k = list(map(int,input().split()))
        if k==1:
            print(n)
        else:
            head = build(n)
            pre = None
            cur = head
            while cur.next != cur:
                for i in range(k-1):
                    pre = cur
                    cur = cur.next
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            print(cur.val)
    except:
        break
