class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        total = 0
        def dfs(root):
            nonlocal total
            if root == None:
                return
            if low <= root.val <= high:
                total += root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return total