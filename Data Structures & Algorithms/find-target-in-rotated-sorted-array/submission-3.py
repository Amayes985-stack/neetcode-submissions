class Solution:
    def search(self, nums: List[int], target: int) -> int:

        top, bottom = 0, len(nums) - 1 

        while top <= bottom : 

            mid = (bottom + top) // 2 

            if nums[mid] == target : 

                return mid 

            if nums[top] <= nums[mid] : 

                #Check the conditions

                if target > nums[mid] or target < nums[top] : 

                    top = mid + 1 

                else : 

                    bottom = mid - 1 

                

            else : 

                if target < nums[mid] or target > nums[bottom] : 

                    bottom = mid - 1 

                else : 

                    top = mid + 1 

        return -1  
        