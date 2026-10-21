class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #Result , stack 

        result = [0] * len(temperatures) 

        stack = [] 

        #Loop through the elements of the temperatures array 

        for i, t in enumerate(temperatures) : 

            #As long as my stack is not empty and the tmp > top of the stack 

            while stack and t > stack[-1][0] : 

                stackT, stackIndx = stack.pop() 

                result[stackIndx] = i - stackIndx #number of days 

            stack.append((t, i)) 

        return result 


        