for _ in range(int(input())):
    s = input()
    dit = {"one":0,"two":0,"three":0}
    if len(s) == 3:
        for i in dit:
            for j in range(len(s)):
                if s[j] == i[j]:
                    dit[i] += 1
        if dit["one"] > dit["two"]:
            print(1)
        else:
            print(2)
    else:
        print(3)
