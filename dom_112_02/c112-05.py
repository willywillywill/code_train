def f_s(s):
    s = s.replace(",","")
    s = s.replace(".","")
    return len(s)


s = list(map(f_s, input().split()))
print(max(s))


"""
Hello, nice to see you.

"""