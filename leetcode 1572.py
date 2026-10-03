mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
res = 0


for i in range(n):
    res += mat[i][i]
    res += mat[i][n-1-i]


if n%2 == 1:
    res -= mat[n//2][n//2]
print(res)
