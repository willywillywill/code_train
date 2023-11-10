while 1:
    try:
        s = input()
        lst = []
        for i in s[::-1]:
            if i not in lst:
                lst.append(i)
        print("".join(lst[::-1]))
    except:
        break

"""
abcdabc
cde12dqceq2
"""