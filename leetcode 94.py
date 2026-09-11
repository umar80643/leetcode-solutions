class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree=[]
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            tree.append(root.val)
            dfs(root.right)
        dfs(root)
        return tree