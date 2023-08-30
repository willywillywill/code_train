
stack = []
s = list(input())
arr = []
while s:
    ss = s.pop(0)
    if ss == "(":
        if stack[-1] == ")":
            pass
    elif ss == ")":
        if stack[-1] == "(":
            stack.pop(-1)