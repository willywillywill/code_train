def maximalRectangkeSum(m):
    if not m:
        return 0
    rows,cols = len(m), len(m[0])
    max_sum = 0
    for i in range(rows):
        for j in range(cols):
            if m[i][j] in (1,2):
                for k in range(i, rows):
                    for l in range(j, cols):
                        if all(m[x][y] in (1,2) for x in range(i,k+1) for y in range(j,l+1)):
                            sub_m_sum = sum(m[x][y] for x in range(i,k+1) for y in range(j,l+1))
                            max_sum = max(max_sum, sub_m_sum)
    return max_sum

input_str = [[1]]
print(maximalRectangkeSum(input_str))