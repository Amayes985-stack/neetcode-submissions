class Solution:
    def findMin(self, nums: List[int]) -> int:

        top, bottom = 0, len(nums) - 1 

        while top < bottom : 

            mid = top + (bottom - top) // 2 

            #Check with the right or left pointer 

            if nums[mid] < nums[bottom] : 

                bottom = mid 

            else : 

                top = mid + 1 

        return nums[top]
        