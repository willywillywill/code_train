

lst = input().replace("(","").replace(")","").replace("/","//").split()
lst = [ int(i) 
       if i not in ["+","-","*","//"]+
       [ chr(i) for i in range(ord("A"),ord("Z")+1) ]+
       [ chr(i) for i in range(ord("a"),ord("z")+1) ] else i 
       for i in lst ]
while 1:
    try:
        a,_,c = input().split()
        idx = lst.index(a)
        lst[idx] = int(c)
    except:
        break




for i in range(len(lst)-1,-1,-1):
    if (len(lst[i:i+3])==3) and \
        (lst[i:i+3][0] in ["+","-","*","//"]) and \
        (lst[i:i+3][1] not in ["+","-","*","//"]) and \
        (lst[i:i+3][2] not in ["+","-","*","//"]):

        l = lst[i:i+3]
        lst[i] = eval(str(l[1])+l[0]+str(l[2]))
        del lst[i+1:i+3]

print(lst[0])

"""
( + 4 ( * x 7 ) )
x = 5
"""