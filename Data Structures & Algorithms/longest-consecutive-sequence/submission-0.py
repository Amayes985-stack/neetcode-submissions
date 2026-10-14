class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums) 

        longestSeq = 0 

        for num in nums : 

            length = 0 

            while (num + length) in numSet : 

                length += 1 

            longestSeq = max(longestSeq, length)  

        return longestSeq

        


        


        