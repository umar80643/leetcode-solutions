class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def TreeComparision(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return (TreeComparision(left.left, right.left) and TreeComparision(left.right, right.right))

        if not subRoot:
            return True
        if not root:
            return False
        if TreeComparision(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




