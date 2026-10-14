class Solution:
    def trap(self, height: List[int]) -> int:

        if not height : 

            return 0 

        head, tails = 0, len(height) - 1 

        result = 0  

        leftMax, rightMax = height[head], height[tails] 

        while head < tails : 

            if leftMax < rightMax : 

                head += 1 

                leftMax = max(leftMax, height[head])

                result += leftMax - height[head] 

            else : 

                tails -= 1 

                rightMax = max(rightMax, height[tails]) 

                result += rightMax - height[tails]

        return result 
