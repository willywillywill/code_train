def f(st,en):
    print(st)
    if st == en:
        return st
    return f(st+1, en)

print(f(0,8))