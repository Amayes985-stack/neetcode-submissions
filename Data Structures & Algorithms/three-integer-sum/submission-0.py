class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = [] 

        nums.sort() 

        for i, a in enumerate(nums) : 


            if i > 0 and nums[i-1] == a : 

                continue 

            head, tails = i + 1 , len(nums) - 1 

            while head < tails : 

                threeSum = a + nums[head] + nums[tails] 

                if threeSum > 0 : 

                    tails -= 1 

                elif threeSum < 0 : 

                    head += 1 

                else : 

                    result.append([a, nums[head], nums[tails]]) 

                    head += 1 

                    tails -= 1 

                    while nums[head] == nums[head-1] and head < tails : 

                        head += 1 

        return result 

        