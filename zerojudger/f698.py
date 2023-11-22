lst = list(input().split())
stack = []
while lst:
    k = lst.pop(0)
    if k in ["+","-","*","/"]:
        k = k.replace("/","//")
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(str(eval(b+k+a)))
    else:
        stack.append(k)
print(stack[-1])

"""
1 2 3 * +
"""