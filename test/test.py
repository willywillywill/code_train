
s = input()
s = s.replace("V","1")
s = s.replace("F","0")
print(eval(s))

"""
(V|V)&F&(F|V)
"""