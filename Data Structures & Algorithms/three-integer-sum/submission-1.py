class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort the array in question 
        result = []

        nums.sort()

        #array to store the result 

       

        #fix the first pointer to nums[i]

        for i, a in enumerate(nums): 

            #check if the index is not out if bound 
            if a > 0 : 

                break 

            if i > 0 and a == nums[i-1]: 

                continue 

                #right and left pointer 

            l, r = i+1, len(nums) - 1 

                #as long as the two poijters dont oveeride /
            while l < r :  

                threeSum = a + nums[l] + nums[r]

                    #Move the pointers 

                if threeSum > 0 : 

                    r -= 1 

                elif threeSum < 0 : 

                    l += 1 

                else :  

                    result.append([a, nums[l], nums[r]])
                    l +=1 

                    r-= 1 

                    while nums[l] == nums[l - 1] and l < r : 

                        l+=1 

        return result 






        