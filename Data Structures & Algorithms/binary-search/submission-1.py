class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #First of all compute the middle value 

        l, r = 0, len(nums) - 1 

        #compute the middle value 

        while l <= r : 

            middle = l + ((r - l) // 2 )

            #check the middle value 

            if nums[middle] > target  : 

                r = middle - 1 

            elif nums[middle] < target  : 

                l = middle + 1 

            else : 

                return middle

        return -1 
        