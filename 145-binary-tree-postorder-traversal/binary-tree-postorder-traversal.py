# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive sol
        # res = []
        # def postorder(root):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        # postorder(root)
        # return res

        # iterative sol
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        res.reverse()
        return res