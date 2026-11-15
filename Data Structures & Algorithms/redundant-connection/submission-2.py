class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        #Cycle detection with an adjacency list 

        n = len(edges) 


        adj = [ [] for _ in range(n + 1)] 

        def dfs(node, par) : 

            #If the node is visited -> return True 

            if visit[node] : 

                return True 

            visit[node] = True 

            for nei in adj[node] : 

                if nei == par : 

                    continue 

                if dfs(nei, node) : 

                    return True 

            return False 


        #Build Adjacenct list 

        for u, v in edges : 

            adj[u].append(v) 

            adj[v].append(u) 

            visit = [False] * (n + 1) 

            if dfs(u, -1) : 

                return [u, v] 


        return []

            
        