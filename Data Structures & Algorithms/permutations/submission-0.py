class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # For our results right now 
        self.result = [] 

        #We would perform the backtrack 
        self.backtrack([], nums, [False] * len(nums)) 

        #We will only return the result at the end of the day (Which happens to be the output)
        return self.result 

#We will perform the backtrack on our permutation array, nums array and the pick array to tell if it's right or wrong to pick 
    def backtrack(self, perm : List[int], nums: List[int], pick: List[bool]) : 

        #If our array has the same length of our nums ==> Base case 
        if len(perm) == len(nums) : 

            self.result.append(perm[:]) #We append the permutation to our result 

            return  

        #Otherwise 

        for i in range(len(nums)) : 

            #We will loop through the array of nums and pick to check the elements that hadn't been picked up yet 

            #If I hadn't picked it, then we will pick it 

            if not pick[i] : 

                #Append the number to the permutation
                perm.append(nums[i]) 

                #We say that it's true
                pick[i] = True 

                #Perform the backtrack 
                self.backtrack(perm, nums, pick) 

                #We lear the array 
                perm.pop() 
                
                pick[i] = False 

        