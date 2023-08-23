stack = []
s = input().split()
for i in s:
    if i.isdigit():
        stack.append(int(i))
    elif len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        num = str(b) + i + str(a)
        stack.append(eval(num))
    print(stack[0])
"""
3 2 5 * + 9 -
"""
