in1 = input()
stack = []
out = ""
for i in in1:
    if i=="(":
        if stack:
            stack.pop()
            stack.append("(")
            out+="*"
    elif i==")":
        if stack:
            stack.pop()
            out.append("*")
        else:
            out+="?"
    else:
        out+="="
print(out)

"""
A(B+C))/(()D
"""