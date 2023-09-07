n = int(input()) #次數
for i in range(n):
    a1, a2 = list(map(str, input().split())) # a1,a2 輸入正整數
    
    if len(a1) != len(a2):          # 比較字串大小，如果不一樣大，把較小的前面補零
        if len(a1) > len(a2):       
            o = len(a1)-len(a2)
            a2 = "0"*o + a2
        else:
            o = len(a2)-len(a1)
            a1 = "0"*o + a1
    c = 0      #進位值
    up = 0     #進位的次數

    a1 = a1[::-1] #從右邊算 055 -> 5  5  0
    a2 = a2[::-1] #               ^1 ^2 ^3
 
    for j in range(len(a1)):  #每一位相加
        k1 = int(a1[j])
        k2 = int(a2[j])

        if (k1+k2+c) >9:      # 此位相加大於九
            c=1
            up +=1            # 進位的次數+1
        else:
            c=0
        
    print(up) 