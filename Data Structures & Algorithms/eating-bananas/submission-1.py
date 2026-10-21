class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Eating the max speed over there 

        l, r = 1, max(piles) 

        result = r 

        #As long as the two pointers don't meet up 

        while l <= r : 

            k = (l + r) // 2 

            totalTime = 0 

            #For every pile 

            for p in piles : 

                totalTime += math.ceil(float(p) / k) #speed of completion 

            if totalTime <= h : 

                result = k 

                r = k - 1 

            else :

                l = k + 1 

        return result 
        