class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''

            Indices over there , if there's no indices -> return None 

            Brute force : 

            1- Two pointers or indices starting at a different position 

            2- Loop through and test every single case of it 

            3- If there's a solution => return the indices , otherwise return empty list  

            Problem : Brute Force Solution => O(n^2) time complexity, O(1) space complexity 

            [3, 4, 5, 6], target = 7 

            Another approach : Using a HashMap or a hashSet , why ?? 

            Search = O(1) 

            Insert and removal = O(1) 

            Index = Element pointing to it | Key = It complement 

            [3, 4, 5, 6]            target = 7

            complement = target - 3 

            if the complement is in the hashmap, insert it indice and return it 

            Otherwise return the empty list 

        '''

        hashMap = {} 

        for i, n in enumerate(nums) : 

            complement = target - nums[i] 

            #If the complement is in the hashMap => return it index 

            if complement in hashMap : 

                return [hashMap[complement], i] 

            hashMap[n] = i

        return indices_index 


        