import datetime

while 1:
    try:
        y,m,d = list(map(int,input().split()))
        date1 = datetime.date(y,m,d)
        y,m,d = list(map(int,input().split()))
        date2 = datetime.date(y,m,d)
        l = [date1,date2]
        print((max(l)-min(l)).days)
    except:
        break