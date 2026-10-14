class Solution:
    def isPalindrome(self, s: str) -> bool:

        sre = "".join(s) 

        head = 0 

        tails = len(sre) - 1 

        while head < tails :  

            while head < tails and not self.alphanum(sre[head]) : 

                head += 1 

            while tails > head and not self.alphanum(sre[tails]) : 

                tails -= 1              

            if sre[head].lower() != sre[tails].lower() : 

                return False 

            head = head + 1 

            tails = tails - 1 

        return True 

    def alphanum(self, c) : 

        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or  
                ord('0') <= ord(c) <= ord('9') )
        