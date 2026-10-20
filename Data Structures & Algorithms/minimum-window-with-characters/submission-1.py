class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #Edge case : If the window is empty ==> return empty chat 

        if t == "" : 

            return "" 

        #Hashmap with frequency and sliding window 

        countT, window = {}, {} 

        for c in t : #For every character in t 

        #Map the letter with its frequency for sure 

            countT[c] = 1 + countT.get(c, 0) 

        have, need = 0 , len(countT) 

        #Two pointers or flags to track 

        result, lenRes = [-1, -1], float("infinity") 

        l = 0 #Left pointer 

        for r in range(len(s)) :  #right pointer moving 

            c = s[r] #the character c will point to the current elem in sliding window 

            window[c] = 1 + window.get(c, 0) #The size of the window increases 

            #If there are characters in the sliding window of t 

            if c in countT and window[c] == countT[c] : 

                #tell that the string have a letter of t 

                have += 1 

            #As long as we find a string that has all of T inside 

            while have == need : 

                if (r - l + 1 ) < lenRes : 

                    result = [l, r] 

                    lenRes = r - l + 1 



                window[s[l]] -= 1 #If not, shrink the size of the window 

            #If the beginning of the window is in t and less than what's int : -= 1 

                if s[l] in countT and window[s[l]] < countT[s[l]] : 

                    have -= 1 

            #Update the count 

                l += 1
        l, r = result 

        return s[l : r + 1] if lenRes != float("infinity") else ""








       

            

            





        



        
        