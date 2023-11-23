import datetime

for _ in range(int(input())):
    t1 = datetime.datetime(year=1970, month=1, day=1)
    t2 = datetime.timedelta(days=int(input()))
    print(str(t1+t2).split()[0])