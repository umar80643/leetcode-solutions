tree = []
def dfs(root):
    if root == None:
        return
    tree.append(root.val)
    dfs(root.left)
    dfs(root.right)


dfs(root)
return tree