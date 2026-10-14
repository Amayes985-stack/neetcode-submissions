class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        top , bottom = 1, max(piles) 

        result = bottom 

        while top <= bottom : 

            k = (top + bottom ) // 2 

            TotalTime = 0 

            for p in piles : 

                TotalTime += math.ceil(float(p) / k) 

            if TotalTime <= h : 

                result = k 

                bottom = k - 1 

            else : 

                top = k + 1 

        return result 
        