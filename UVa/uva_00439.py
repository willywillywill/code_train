
from collections import deque

move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def bfs(start, end):
    queue = deque([start])
    visited = set()
    distance = {start: 0}
    while queue:
        current = queue.popleft()
        if current == end:
            return distance[current]
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in move:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < 8 and 0 <= next_y < 8 and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                distance[(next_x, next_y)] = distance[(x, y)] + 1
    return -1

while True:
    try:
        start, end = input().split()
        s_ = start
        e_ = end
        start = (ord(start[0]) - ord('a'), int(start[1]) - 1)
        end = (ord(end[0]) - ord('a'), int(end[1]) - 1)
        print(f'To get from {s_} to {e_} takes {bfs(start, end)} knight moves.')
    except:
        break
