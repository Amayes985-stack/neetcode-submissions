class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Cycle detection with DFS and map every single course to its prerequisites

        preMap = {i: [] for i in range(numCourses)} 

        for crs, pre in prerequisites : 

            preMap[crs].append(pre)

        #Visiting set 

        output = []

        visiting, cycle = set() , set()

        def dfs(crs) : 

            if crs in cycle : 

                return False #If cycle is detected -> False 

            if crs in visiting : 

                return True 

            cycle.add(crs) 

            for pre in preMap[crs] : 

                if dfs(pre) == False : 

                    return False 

            cycle.remove(crs) 

            visiting.add(crs) 

            output.append(crs)

            return True 

        for c in range(numCourses) : 

            if dfs(c) == False  : 

                return [] 

        return output