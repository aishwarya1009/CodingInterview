from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def fn(node):
            if node:
                fn(node.left)
                ans.append(node.val)
                fn(node.right)

        fn(root)
        return ans
