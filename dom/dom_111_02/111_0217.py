s = input()
s = [ i for i in s if i in ["(",")"] ]
num = 0
stack = []
for i in s:
    if i=="(":
        stack.append(i)
    else:
        num = max(len(stack),num)
        stack.pop()
print(num)

"""

(1+(2*3)+((8)/4))+1
"""