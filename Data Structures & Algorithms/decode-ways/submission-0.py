class Solution:
    def numDecodings(self, s: str) -> int:

        # 1012 -> 10 1 2 -> J A B       Count += 1 

        # 1 01 2 -> Invalid (Because it contains a leading 0 ) X

        # 10 12 -> JL       Count += 1 


        #01 -> Invalid because it starts with a leading 0 

        #1001 -> 100 1 X(invalid) -> 10 01 X(invalid) -> Output = 0 

        #If we start with a leading 0 -> It's already a bad move 


        #Native approach (Brute Force) -> To test every combinaision possible 


        #If our string starts with 0 -> it's already done for 

        
        #Execution Tree -> 


        """  
                                1012 

                        1                   012 

                    10                          12 

                10            1                      2   
        
        
        """


        dp = {len(s) : 1 } 

        def dfs(i) : 

            if i in dp : 

                return dp[i] 

            if s[i] == "0" : 

                return 0 

            
            result = dfs(i + 1)

            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456")) :  

                    result += dfs(i + 2) 

            dp[i] = result 

            return result  

        return dfs(0)
        
        