# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        result = []

        #Use dfs preorder 

        def dfs(node) : 

            if not node : 

                result.append("N") 

                return 

            result.append(str(node.val)) 

            dfs(node.left) 

            dfs(node.right)

        dfs(root) 

        return ",".join(result)


        #if node is null ==> append N 

        #Or append node value 

        #Recursively join left child and right child 

        #join the list with commas 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        #Split the string into a list of values 

        vals = data.split(",") 

        self.i = 0 

        #Index to process values in order for sure (DFS ) 

        def dfs() : 

            if vals[self.i] == "N" : 

                self.i += 1 

                return None 

            node = TreeNode(int(vals[self.i])) 

            self.i += 1 

            node.left = dfs() 

            node.right = dfs() 

            return node 

        return dfs()

        #If the current value is N -> return None 

        #Create a node 

        #Build left tree 

        #Build right tree 

        #Return the root 
