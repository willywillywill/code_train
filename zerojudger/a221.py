# OK !!!

outtype=[
    "Wrong Answer",                                          # 位置0 都不一樣          a+b = 0
    "Output Format Error",                                   # 位置1 空格不一樣        a+b = 1
    "Yes",                                                   # 位置2 都一樣            a+b = 2
    lambda x,y: list(x) == list(y),                          # 判斷是否一樣            a: 1 / 0  
    lambda x,y: ''.join(x.split()) == ''.join(y.split())     # 去除空格並判斷是否一樣   b: 1 / 0
        ]


for t in range(int(input())):
    temp=[input(),input()]
    a1 = outtype[3](temp[0],temp[1])
    a2 = outtype[4](temp[0],temp[1])

    print("Case %d:"%(t+1), outtype[a1+a2])


