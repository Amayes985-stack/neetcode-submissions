class Solution:
    def findMin(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1 

        current_min = float("inf") 

        while start < end : 

            middle = start + (end - start) // 2 

            current_min = min(current_min, nums[middle]) 

            if nums[middle] > nums[end] : 

                start = middle + 1 

            else : 

                end = middle - 1 

        return min(current_min, nums[start])
        