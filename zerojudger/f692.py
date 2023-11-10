"""
in1 = input().split()
li = []
func = {
    "+": int.__add__,
    "-": int.__rsub__,
    "*": int.__mul__,
    "/": int.__rfloordiv__
}
for i in in1:
    li.append( int(i) if i not in "+-*/" else func[i](li.pop(),li.pop()) )
print(li[0])
"""

"""
"""
stack = []
for i in input().split():
    if i in "+-*/":
        i = i.replace("/","//")
        expr = "%s%s%s"%(stack.pop(-2),i,stack.pop(-1))
        stack.append(eval(expr))
    else:
        stack.append(int(i))
print(stack[0])

"""
1 2 3 * +
2 5 + 4 * 6 3 / -
"""