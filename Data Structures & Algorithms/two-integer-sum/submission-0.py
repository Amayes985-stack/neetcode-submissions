class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        previousMap = {} 

        for i, n in enumerate(nums) : 

            diff = target - n 

            if diff in previousMap : 

                return[previousMap[diff], i] 

            previousMap[n] = i 
        