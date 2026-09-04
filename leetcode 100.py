class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        if not p and not q:
10            return True
11        if not p or not q:
12            return False
13        return (
14            p.val == q.val
15            and self.isSameTree(p.left , q.left)
16            and self.isSameTree(p.right, q.right)
17        )

