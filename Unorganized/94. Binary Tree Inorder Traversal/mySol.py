# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if root:
            # Traverse the left subtree
            result += self.inorderTraversal(root.left)
            # Visit the root (current node)
            result.append(root.val)
            # Traverse the right subtree
            result += self.inorderTraversal(root.right)
        return result
        
class IterativeSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go as deep as possible on the left subtree
            while current:
                stack.append(current)
                current = current.left
            
            # Process the current node (popping from stack)
            current = stack.pop()
            result.append(current.val)
            
            # Explore the right subtree
            current = current.right
        
        return result