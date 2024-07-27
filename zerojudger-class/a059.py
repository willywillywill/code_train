for _ in range(int(input())):
    a = int(input())
    b = int(input())
    s = 0
    for i in range(a,b+1):
        if int(i**0.5)==i**0.5:
            s += i
    print(f"Case {_+1}:", s)
