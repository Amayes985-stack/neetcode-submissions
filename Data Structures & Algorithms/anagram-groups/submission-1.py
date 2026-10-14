class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) 

        for string in strs : 

            count = [0] * 26 

            #Map every character with it frequency 

            for character in string : 

                count[ord(character) - ord('a')] += 1 

            #Create a tuple with stringd that share the same count 

            result[tuple(count)].append(string)

        return list(result.values()) #Return the triplets 


        

  
        