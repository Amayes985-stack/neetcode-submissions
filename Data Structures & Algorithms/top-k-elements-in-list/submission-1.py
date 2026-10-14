class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #define count and frequency 

        count = {} #HashMap to map [number -> frequency] 

        freq = [ [] for i in range(len(nums) + 1)] #Frequency buckets where we will sort the  result there 

        for num in nums : 

            #Map every single number to it frequency 

            count[num] = 1 + count.get(num,0 ) #If you find a value, add it otherwise put 0 

        #Once we're done with that, create frequency bucket with indexes and their frequency 

        for num, cnt in count.items() : 

            freq[cnt].append(num) 

        result = [] 

        #Loop through the frequency array until k and pop the results from the right to left

        for i in range(len(freq) -1 , 0, -1) : 

            for num in freq[i] : 

                result.append(num) 

                #add the numbers until you reach k and then return th result 

                if len(result) == k : 

                    return result  

        