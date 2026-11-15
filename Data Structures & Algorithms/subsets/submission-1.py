class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #result and subsets 

        result , subsets = [], [] 

        def dfs(i) : 

            #When to append 

            if i >= len(nums) : 

                result.append(subsets.copy()) #copying the subset 

                return 

            subsets.append(nums[i]) 

            dfs(i + 1) 

            subsets.pop() 

            dfs(i + 1) 


        dfs(0) 

        return result 
        