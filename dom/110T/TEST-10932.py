import datetime

for _ in range(int(input())):
    s = datetime.datetime(1970, 1,1)
    d = datetime.timedelta(days=int(input()))
    s = s+d
    print(str(s).split()[0])