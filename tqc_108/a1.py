minx = int(input())
sec = int(input())
km = int(input())

sec = minx*60+sec
h = sec/60/60
l = km/1.6/h
print("Speed = %.1f"%(l))
