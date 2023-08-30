m = int(input())
s = int(input())
km = int(input())

s += m*60
i = km/1.6
s = s/60/60
speed = i/s

print("Speed = %.1f"%(speed))