class node:
    def __init__(self, v=None):
        self.v = v
        if v:
            self.f = self.v.lower()
        self.t = 1
        self.next = None
    def Add(self, v):
        if not self.v:
            self.v = v
            self.f = v.lower()
            return

        if self.f == v.lower():
            self.t += 1
        else:
            if self.next:
                self.next.Add(v)
            else:
                self.next = node(v)

    def Add_idx(self, v, idx, ptr):
        if idx != 1:
            self.next.Add_idx(v, idx-1, self.next)
        else:
            k = self.next
            ptr.next = node(v)
            ptr.next.next = k
    def Long(self):
        if self.next:
            return self.next.Long()+1
        return 1
    def Val(self, l):
        l.append(self.f)
        if self.next:
            self.next.Val(l)
    
class Main:
    def __init__(self):
        self.Link_list = node()
        while 1:
            l = input().split()
            if l == ["#Finish"]:
                break
            for i in l:
                self.Insert(None, i)
        
        self.Link_len = self.Link_list.Long()

        while 1:
            cmd = input()
            if cmd == "#Print":
                self.Print(self.Link_list)
            elif cmd == "#Insert":
                idx = int(input())
                v = input()
                self.Insert(idx, v)
            elif cmd == "#Add":
                v = input()
                self.Insert(None, v)
            elif cmd == "#Exit":
                break

    def Print(self, root):
        if root:
            print("%s, %s"%(root.v,root.t))
            self.Print(root.next)
    def Insert(self, idx, v):
        if idx:
            if idx <= self.Link_len:
                val = []
                self.Link_list.Val(val)
                if v.lower() in val:
                    self.Link_list.Add(v)
                else:
                    self.Link_list.Add_idx(v,idx,self.Link_list)
        else:
            self.Link_list.Add(v)
            
        self.Link_len = self.Link_list.Long()

Main()

"""
Happy birthday FJU
I love FJU
#Finish
#Print
#Insert
10
Taipei
#Insert
3
Christmas
#Insert
2
Love
#Print
#Add
fju
#Add
CSIE
#Print
#Exit
"""