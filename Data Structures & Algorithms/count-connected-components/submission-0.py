class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #Union Find , go to every node and find the parent and then find the family 

        par = [i for i in range(n)] 

        rank = [1] * n 

        def find(n1) : 

            result = n1 

            while result != par[result] :

                par[result] = par[par[result]]  
                result = par[result]

            return result 


        def union(n1, n2) : 

            #find root parents 

            p1, p2 = find(n1), find(n2) 

            if p1 == p2 : #they have the same parent 

                return 0 

            if rank[p2] > rank[p1] : 

                par[p1] = p2 

                rank[p2] += rank[p1] 

            else : 

                par[p2] = p1 

                rank[p1] += rank[p2] 

            return 1 

        result = n 

        for n1, n2 in edges : 

            result -= union(n1, n2) 

        return result 






        