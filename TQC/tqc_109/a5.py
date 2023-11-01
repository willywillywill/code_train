# NO
# 6:02

s = list(input())

stack = []
arr = []
out = []

while s:
    ss = s.pop(0)
    if ss == "(":
        stack.append(ss)
        out.append("*")
        arr.append(len(out)-1)
    elif ss == ")":
        if stack:
            stack.pop(-1)
            out.append("*")
            arr.pop(-1)
        else:
            out.append("?")
    else:
        out.append("=")
for i in arr:
    out[i] = "?"
print("".join(out))