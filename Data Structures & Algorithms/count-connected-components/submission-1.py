class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #Code it with an adjacency list 

        adj = [ [] for _ in range(n)] 

        visit = [False] * n 

        for u, v in edges : 

            adj[u].append(v) 

            adj[v].append(u) 

        #Building the adjacency matrix for sure 

        def dfs(node) : 

            for nei in adj[node] : 

                #If not visited 

                if not visit[nei] : 

                    visit[nei] = True 

                    dfs(nei) 

        result = 0 

        for node in range(n) : 

            if not visit[node] : 

                visit[node] = True 

                dfs(node) 

                result += 1 

        return result 
        