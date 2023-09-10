to_day = 10


mony = 1
day_mony = [0]
while len(day_mony) < to_day:
    for i in range(mony):
        day_mony.append(mony)
    mony+=1
print(sum(day_mony))
