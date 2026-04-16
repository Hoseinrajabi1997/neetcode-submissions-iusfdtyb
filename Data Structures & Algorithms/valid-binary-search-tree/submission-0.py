# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isv(root, mn,mx):
            if not root:
                return True
            
            if root.val <= mn or root.val >= mx:
                return False

            return isv(root.left, mn, root.val) and isv(root.right, root.val, mx)
        return isv(root, -1001, 1001)