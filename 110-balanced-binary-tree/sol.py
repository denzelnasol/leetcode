from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculateHeight(root) >= 0
    
    def calculateHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        leftHeight, rightHeight = self.calculateHeight(node.left), self.calculateHeight(node.right)
        
        if abs(leftHeight - rightHeight) > 1 or leftHeight < 0 or rightHeight < 0: 
            return -1
        
        return max(leftHeight, rightHeight) + 1
        