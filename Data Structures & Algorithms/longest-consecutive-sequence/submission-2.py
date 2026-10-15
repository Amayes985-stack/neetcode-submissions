class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       numSet = set(nums) 

       longest = 0 

       for num in numSet : 

            if (num - 1) not in numSet : #If the beginning of a sequence is not here ==> beginning of a sequence 

                length = 1 

            #Keep the streak 

                while (num + length) in numSet : 

                    length += 1 

                longest = max(length, longest)

       return longest
        