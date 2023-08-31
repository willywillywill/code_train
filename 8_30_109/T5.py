
stack = []
s = list(input())
arr = []
k = []
while s:
    ss = s.pop(0)

    if ss == "(":
        stack.append(ss)
        arr.append("*")
        k.append(len(arr)-1)
    elif ss == ")":
        if stack:
            stack.pop(-1)
            arr.append("*")
            k.pop(0)
        else:
            arr.append("?")
    else:
        arr.append("=")
    print(stack)
for i in k:
    arr[i] = "?"
print("".join(arr))


"""
(A+B)(C+D))+A-B(D+E)(T
((A+5)+(B-3)/2))
"""