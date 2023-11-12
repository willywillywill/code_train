class node:
    def __init__(self,val=None):
        self.lst = [val]
    def __call__(self,val):
        self.lst.append(val)
    def pop(self):
        self.lst.pop(-1)
    
    def search(self, val, idx=0):
        if val in self.lst[idx]:
            self.lst[idx](val)
        else:
            if idx < len(self.lst):
                self.search(val,idx+1)
            else:
                self.__call__(node())
                self.lst[-1](val)

t = int(input())
que = node()
for _ in range(t):
    que(node())
que(1)

print(que.lst)
#que = list(map(int,input().split()))[1:]
#print(que)