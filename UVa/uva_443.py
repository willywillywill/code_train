import sys
humble_numbers = [1]
i, j, k, m = 0, 0, 0, 0
while len(humble_numbers) < 5843:
    next_humble = min(humble_numbers[i] * 2, humble_numbers[j] * 3, humble_numbers[k] * 5, humble_numbers[m] * 7)
    if next_humble == humble_numbers[i] * 2:
        i += 1
    if next_humble == humble_numbers[j] * 3:
        j += 1
    if next_humble == humble_numbers[k] * 5:
        k += 1
    if next_humble == humble_numbers[m] * 7:
        m += 1
    humble_numbers.append(next_humble)

def ordinaltg(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

for i in sys.stdin:
    i = int(i)
    if i == 0:
        break
    print(f"The {ordinaltg(i)} humble number is {humble_numbers[i-1]}.")
