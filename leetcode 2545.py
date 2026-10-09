score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2


def get_score(row):
    return row[k]


score.sort(key=get_score, reverse=True)

print(score)