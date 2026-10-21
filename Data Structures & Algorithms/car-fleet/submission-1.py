class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #pair eac car position with its speed

        pair = [(p,s) for p, s in zip(position, speed)]

        #sort the cars in ascending order 

        pair.sort(reverse=True)

        stack = []

        #for every car 

        for p, s in pair : 

            

        #compute the time it takes to reach the target 

            stack.append((target - p) / s) 

            if len(stack) >= 2 and stack[-1] <= stack[-2] : 

                stack.pop() 

        return len(stack)

        #Append it in a stack 

        #If the new time is <= time before it -> pop it 

        #return the stack size 


        