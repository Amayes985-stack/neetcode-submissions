class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = [] 
        q = deque() 

        head = tails = 0

        while tails < len(nums) : 

            while q and nums[q[-1]] < nums[tails]: 

                q.pop()

            q.append(tails) 

            if head > q[0] : 

                q.popleft() 

            if (tails + 1) >= k : 

                result.append(nums[q[0]]) 

                head += 1 

            tails += 1 

        return result 