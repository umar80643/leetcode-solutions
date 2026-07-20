

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4

m = len(grid)
n = len(grid[0])

total = m * n
k %= total

ans = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        old_index = i * n + j
        new_index = (old_index + k) % total
        row = new_index // n
        col = new_index % n

        ans[row][col] = grid[i][j]


print(ans)