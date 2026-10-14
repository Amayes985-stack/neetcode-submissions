class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {} 

        head = 0 

        maxf = 0 


        for tails in range(len(s)) : 

            count[s[tails]] = 1 + count.get(s[tails], 0) 

            maxf = max(maxf, count[s[tails]]) 

            if (tails - head + 1 ) - maxf > k : 

                count[s[head]] -= 1 

                head += 1 

        return (tails - head + 1)
        