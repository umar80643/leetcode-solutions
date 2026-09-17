class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        sum_val =0
        maxdepth = -1
        def dfs(root , depth):
            nonlocal sum_val , maxdepth
            if root is None:
                return
            if root.left is None and root.right is None:
                if depth > maxdepth:
                    maxdepth = depth
                    sum_val = root.val
                elif depth == maxdepth:
                    sum_val += root.val
                return

            left = dfs(root.left , depth + 1)
            right = dfs(root.right , depth + 1)
        dfs(root ,0)
        return sum_val