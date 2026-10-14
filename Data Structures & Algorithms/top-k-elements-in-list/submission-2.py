class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ''' 
        Top frequent element within the Elements 

        k = 2 (it frequency is 2 )

        Main idea : Build a hashmap (element, count) 

        - If the element isn't within the hashMap => add it and update the count 

        - Otherwise update it count already 

        1, 1 

        2, 2 

        3, 3 

        k = 2

        Then for the count and append an array for the results 

        You'll append only the values that are >= k 

        3 - 2 = 1 

        2 - 2 = 0 (add the 3)



        '''

        #First of all build the frequency map 

        count = {}
        
        freq = [ [] for i in range(len(nums) + 1)]

        #Fill it 

        for num in nums : 

            count[num] = 1 + count.get(num, 0) 

        for num, cnt in count.items() : 

            freq[cnt].append(num) 

        result = [] 

        for i in range(len(freq) - 1, 0, -1) : 

            for num in freq[i] : 

                result.append(num) 

                if len(result) == k : 

                    return result 

   

            #Otherwise update the result of it for sure  


            
        