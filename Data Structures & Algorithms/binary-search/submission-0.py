class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower_bound = 0
        upper_bound = len(nums) - 1 

        while lower_bound <= upper_bound : 

            middle = lower_bound + ((upper_bound - lower_bound // 2 )) 

            if nums[middle] > target : 

                upper_bound = middle - 1 

            elif nums[middle] < target : 

                lower_bound = middle + 1 

            else : 

                return middle 

        return -1 
        

                

        


        