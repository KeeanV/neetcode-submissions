# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(TreeNode,minimum, maximum):
            if not TreeNode:
                return True
            if (TreeNode.val <= minimum or TreeNode.val >= maximum):
                return False
            return valid(TreeNode.left, minimum, TreeNode.val) and valid(TreeNode.right,TreeNode.val, maximum)
        return valid(root, float('-inf'), float('inf'))
        