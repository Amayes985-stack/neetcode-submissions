class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0 

        head, tails = 0, len(heights) - 1 

        while head < tails : 

            area = (tails - head) * min(heights[head], heights[tails])

            result = max(result, area) 

            if heights[head] < heights[tails] : 

                head += 1 

            else : 

                tails -= 1 

        return result 
        