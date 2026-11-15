# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #Check that the nodes are valid 

        def valid(node, left, right) : 

            if not node : 

                return True 

            if not (left < node.val < right) : 

                return False 

            return valid(node.left, left, node.val) and valid(
                
                node.right, node.val, right
                
            ) 


        #Perform the whole thing right after 

        return valid(root, float("-inf"), float("inf")) 



     
