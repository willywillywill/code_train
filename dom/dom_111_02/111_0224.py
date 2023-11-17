st1 = list(input())
st2 = list(input())
st3 = []

while st1 and st2:
    a = st1.pop(0)
    b = st2.pop(0)
    st3.append(a)
    st3.append(b)
while st1:
    st3.append(st1.pop(0))
while st2:
    st3.append(st2.pop(0))  
print("".join(st3))

"""
ab
pqrs

abc
pqr

"""