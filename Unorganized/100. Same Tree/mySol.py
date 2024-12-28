
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None or p.val != q.val:
            return False
         
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Have to and the returns here to check left and right.