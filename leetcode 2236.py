root = [10,4,6]
if root == None:
    print()

ans = root.left.val + root.right.val
if ans == root.val:
    print(True)
else:
    print(False)
