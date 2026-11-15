class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #Cycle detection with DFS and map every single course to its prerequisites

        preMap = {i: [] for i in range(numCourses)} 

        for crs, pre in prerequisites : 

            preMap[crs].append(pre)

        #Visiting set 

        visiting = set() 

        def dfs(crs) : 

            if crs in visiting : 

                return False #If cycle is detected -> False 

            if preMap[crs] == [] : 

                return True 

            visiting.add(crs) 

            for pre in preMap[crs] : 

                if not dfs(pre) : 

                    return False 

            visiting.remove(crs) 

            preMap[crs] = [] 

            return True 

        for c in range(numCourses) : 

            if not dfs(c) : 

                return False 

        return True 
        