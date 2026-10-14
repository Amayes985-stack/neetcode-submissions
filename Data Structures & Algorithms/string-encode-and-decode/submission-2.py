class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs : 

            return "" 

        sizes, result = [], [] 

        for s in strs: 

            sizes.append(len(s)) 

        for sz in sizes : 

            result.append(str(sz)) 

            result.append(',') 

        result.append('#')

        result.extend(strs) 

        return ''.join(result)

        

    def decode(self, s: str) -> List[str]:

        if not s : 

            return [] 

        sizes, result, i = [], [], 0 

        while s[i] != '#' : 

            j = i 

            while s[j] != ',' : 

                j += 1 

            sizes.append(int(s[i:j])) 

            i = j + 1 

        i += 1 

        #Now with the sizes 

        for sz in sizes : 

            result.append(s[i:i+sz])

            i += sz 

        return result

    '''

    ["Hello", "World"] => "Hello World"  

    1- Record the length of each string with a separator -> append all strings together 

    2- Decoding we can read the recorded lengths to know exactly how many characters to extract for each original string 


    Encoding : 

    1- If input is empty => empty string 

    2- Create a list to store the sizes of the strings 

    3- For each string , append it length to the sizes list 

    4- Build by : 

    -> Writing all sizes separated by commas 
    -> Mark the end with a # 

    -> Append the actual string 

    Decoding : 

    1- If encoded string is empty ==> return empty list 

    2- Read chars from the start until reaching # to extract the recorded sizes 

    -> Parse each size until reaching a comma 

    3- After the #, extract the substrings according to the sizes list 

    -> For each side, read that many characters and append the substring to result 

    4- return the list of decoded string 

    '''
