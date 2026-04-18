# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    mx = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")
        def dfs(node):
            if not node:
                return float("-inf")
            nonlocal mx

            res = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            mx = max(mx,left,right,res, res+left,res+right,res+left+right)
            return max(left+res,right+res,res)
        dfs(root)
        return mx