from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right






class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, runningSum: int = 0) -> bool:
        
        if not root:
            return False
        
        runningSum+= root.val
        
        if root.left:
            return self.hasPathSum(root.left, targetSum, runningSum)
        if root.right:
            return self.hasPathSum(root.right, targetSum, runningSum)
        
        if runningSum == targetSum:
            return True
        
        return False