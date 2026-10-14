class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0 

        charSet = set() 

        head = 0  

        for tails in range(len(s)) : 

            while s[tails] in charSet : 

                charSet.remove(s[head]) 

                head += 1 

            charSet.add(s[tails])

            result = max(result, tails - head + 1) 

        return result  


        