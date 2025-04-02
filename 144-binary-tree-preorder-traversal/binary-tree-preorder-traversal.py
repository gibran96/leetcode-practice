# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive
        # res = []
        # def preorder(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        # return res

        #iterative
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res