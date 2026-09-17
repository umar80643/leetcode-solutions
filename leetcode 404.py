class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        sum_val = 0

        def dfs(root, isleft):
            nonlocal sum_val
            if root == None:
                return
            if root.left is None and root.right is None and isleft:
                sum_val += root.val
                return

            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, False)
        return sum_val