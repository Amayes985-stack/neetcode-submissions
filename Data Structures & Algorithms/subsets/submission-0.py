class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [] 

        Subset = []

        def dfs(i) : 

            if i >= len(nums) : 

                result.append(Subset.copy())
                return 

            #Include nums[i]
            Subset.append(nums[i]) 

            dfs(i + 1)

            #Not include nums[i]
            
            Subset.pop() 

            dfs(i + 1) 

        dfs(0) 

        return result 

        