# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = [root.val] 

        def dfs(root) : 

            #if not root ==> return null 

            if not root : 

                return 0 

            #Precompute the values 

            leftMax = dfs(root.left) 

            rightMax = dfs(root.right) 

            #Update the counts to compute the path 

            leftMax = max(leftMax, 0) 

            rightMax = max(rightMax, 0) 

            #Result 

            result[0] = max(result[0], root.val + leftMax + rightMax) 

            return root.val + max(leftMax, rightMax) 

        dfs(root) 

        return result[0]
        