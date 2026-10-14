class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {} 

        if len(t) > len(s) : 

            return 0 

        def dfs(i, j) : 

            if j == len(t) : 

                return 1 

            if i == len(s) : 

                return 0 

            if (i, j) in dp : 

                return dp[(i, j)] 

            

            result = dfs(i + 1, j) 

            if s[i] == t[j] : 

                result += dfs(i + 1, j + 1) 

            dp[(i, j)] = result 

            return dp[(i, j)]


        return dfs(0, 0)
        