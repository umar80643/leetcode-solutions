class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        num_nodes =[0]
        def dfs(root):
            if root == None:
                return (0,0)
            n_left , sum_left = dfs(root.left)
            n_right , sum_right = dfs(root.right)
            n = 1 + n_left + n_right
            sum_val = root.val + sum_left + sum_right
            avg = sum_val // n

            if root.val == avg:
                num_nodes[0] += 1
            return [n , sum_val]
        dfs(root)
        return num_nodes[0]