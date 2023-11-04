"""
move a onto b 
move a over b
pile a onto b
pile a over b
quit
"""

def search_val(func):
    def search(**kwargs):  # end val i=0 j=0
        if kwargs["end"] not in lst[kwargs["i"]]:
            kwargs["i"] += 1
            return search(**kwargs)
        elif kwargs["end"] != lst[kwargs["i"]][kwargs["j"]]:
            kwargs["j"] += 1
            return search(**kwargs)
        else:
            if "val" not in kwargs:
                kwargs["val"] = lst[kwargs["i"]][kwargs["j"]+1:]
            return func(**kwargs)
    return search
def search_idx(func): # end i=0
    def search(**kwargs):
        if kwargs["end"] != kwargs["i"]:
            kwargs["i"] += 1
            return search(**kwargs)
        else:
            
            return func(**kwargs)
    return search

@search_val
def chick(**kwargs):
    if kwargs["chick"] in kwargs["val"]:
        return False
    return True
@search_val
def delete(**kwargs): # end val i=0 j=0
    del lst[kwargs["i"]][kwargs["j"]:]
    return kwargs
@search_val
def insert_val(**kwargs):
    lst[kwargs["i"]].append(kwargs["val"])
    return kwargs

@search_idx
def insert_idx(**kwargs):
    lst[kwargs["i"]].append(kwargs["val"])
    return kwargs

def move_onto(a,b):
    del_a = delete(end=a,i=0,j=0)
    del_b = delete(end=b,i=0,j=0)
    for i in del_a["val"]:
        insert_idx(end=i, i=0, val=i)
    for i in del_b["val"]:
        insert_idx(end=i, i=0, val=i)
    insert_idx(end=del_b["i"], i=0, val=del_b["end"])
    insert_val(end=del_b["i"], i=0, j=0, val=del_a["end"])
def move_over(a,b):
    del_a = delete(end=a,i=0,j=0)
    for i in del_a["val"]:
        insert_idx(end=i, i=0, val=i)
    insert_val(end=b, i=0, j=0, val=del_a["end"])
def pile_onto(a,b):
    del_b = delete(end=b, i=0, j=0)
    insert_idx(end=del_b["i"], i=0, val=del_b["end"])
    for i in del_b["val"]:
        insert_idx(end=i, i=0, val=i)
    del_a = delete(end=a, i=0, j=0)
    del_a["val"].insert(0, del_a["end"])
    for i in del_a["val"]:
        insert_val(end=b, i=0, j=0, val=i)

def pile_over(a,b):
    if chick(end=a,i=0,j=0,chick=b):
        del_a = delete(end=a,i=0,j=0)
        del_a["val"].insert(0,del_a["end"])
        for i in del_a["val"]:
            insert_val(end=b, i=0, j=0, val=i)

dit = {
    "move_onto":move_onto,
    "move_over":move_over,
    "pile_over":pile_over,
    "pile_onto":pile_onto
}

n = int(input())
lst = [ [i] for i in range(n) ]
while 1:
    in1 = input().split()
    if "quit" in in1:
        break
    dit["%s_%s"%(in1[0],in1[2])](int(in1[1]),int(in1[3]))    
for i in range(len(lst)):
    print("%d:"%(i),*lst[i])


