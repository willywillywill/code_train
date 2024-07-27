#%% deep copy
# https://docs.python.org/zh-tw/3/library/copy.html
# https://ithelp.ithome.com.tw/articles/10221255

def shallow_copy():
    lst = [[1,2,3],[4,5,6]]
    lst2 = lst[0] 
    # or lst2 = lst.copy()[0]
    lst2[0] = -1 # <- lst 會跟著改變
    
    return lst

def deep_copy():
    import copy
    lst = [[1,2,3],[4,5,6]]
    lst2 = copy.deepcopy(lst)[0]
    # or lst2 = [ i for i in lst[0] ]
    lst2[0] = -1

    return lst
"""
在 vscode 中用 #%% 可以偵錯
好處是定義 function 然後在旁邊的 interactive
寫 python
like -> print(deep_copy()) 
"""