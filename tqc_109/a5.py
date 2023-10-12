in1 = list(input())
stack = []
out = []
k = []
while in1:
    i = in1.pop(0)
    if i=="(":
        stack.append("(")
        out+="*"
        k.append(len(out)-1)
    elif i==")":
        if stack:
            stack.pop(-1)
            k.pop(0)
            out+="*"
        else:
            out+="?"
    else:
        out+="="
for i in k:
    out[i]="?"
print(out)

"""
A(B+C))/(()D
"""