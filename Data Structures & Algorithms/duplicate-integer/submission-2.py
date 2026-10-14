class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Brute force approach : Test every single element and check if there's an equal element 

        #Problem  : O(n^2) 

        ''' 

        How to solve this ?? HASHMAP 

        key, value 

        element, frequency 

        Build a hashMap and update it count 

        1, 1            

        2, 1

        3, 2 

        Search for it, if there's an element with a count == 2 ==> return true , otherwise false 

        '''

        countD = {} 

        for i, n in enumerate(nums) : 

            if nums[i] in countD : 

                #Put it inside 

                return True 

            countD[nums[i]] = i 

            countD[n] = 1 + countD.get(nums[i], 0) 

        return False 




        

  

            


        