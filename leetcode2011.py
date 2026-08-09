operations = ["--X","X++","X++"]
X=0
for operation in operations:
    if operation == "--X" or operation == "X--":
        X = X-1
    elif operation == "++X" or operation == "X++":
        X = X+1
print(X)



