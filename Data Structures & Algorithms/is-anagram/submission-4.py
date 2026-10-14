class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
            Edge case : Empty list ==> anagram 

            Brute force solution here : 

            1- Build a hashMap (key, value) 

            2- Fill the hashMap with the character and it occurences in the list 

            3- Check that every character has the same number of counts ==> return True 

            4- Otherwise return false 


            r , 2           c, 2 
            a, 2            a, 2
            c, 2            r, 2
            e, 1            e, 1 

            For a valid anagram ==> same length and same count of characters 

            j, 1            j, 1
            a, 1            a, 1
            r, 1            m, 1 

            Different characters ==> not anagrams 



        '''

        if len(s) == 0 and len(t) == 0 : 

            return True #Edge case 

        if len(s) != len(t) : 

            return False #Another edge case 
        
        countS, countT = {}, {} #Key(char), val 

        #First of all fill in the hashMap with the counts 

        for i in range(len(s)) : 

            countS[s[i]] = 1 + countS.get(s[i], 0) 

            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

