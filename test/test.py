count = 0

data_length = 3
for i in range(data_length):
    for j in range(data_length):
        for k in range(data_length):
            if i == j or i == k:
                count += 1
print(count % 4)
print(count)