coordinates=[[0,0],[0,1],[0,-1]]
x1, y1 = coordinates[0]
x2, y2 = coordinates[1]
dx = x2 - x1
dy = y2 - y1
for x, y in coordinates[2:]:
    if (y - y1) * dx != (x - x1) * dy:
        print(False)
print(True)
