class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        ''' 
        Longest substring without duplicate characters 

        1- Initialise a sliding windiw starting from the very beginning 

        2- Extend the window and then delete the element right after as soon as we come across a repeating character 

        z   x   y   z   x   y   z 


        windows = set() 

        longest = 0 

        l, r = 0, 1 

        for r in range(n) : 

            if str[r] in windows : 





        '''

        l, total = 0, 0 

        charSet = set() 

        for r in range(len(s)) : 

            while s[r] in charSet : 

                charSet.remove(s[l]) 

                l += 1 

            charSet.add(s[r]) 

            total = max(total, r - l + 1) 

        return total 



