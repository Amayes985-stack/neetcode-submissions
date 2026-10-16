class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #result and 2 pointers initialised 

        maxArea = 0 

        l, r = 0, len(heights) - 1 

        #perform the loop and go through the arrayb

        while l < r : 

            result = (r - l) * min(heights[r], heights[l]) 

            maxArea = max(maxArea, result)

            #moving the right pointers 

            if heights[l] <= heights[r] : 

                l += 1 

            else : 

                r-= 1 

        return maxArea 


        