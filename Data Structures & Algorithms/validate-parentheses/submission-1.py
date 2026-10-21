class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {")" : "(", "]" : "[" , "}" : "{"} 

        stack = [] 

        #For every single character in s :

        for c in s : 

            #For every character in close / open : 

            if c in closeToOpen : 

            #If my stack is not empty and the top of my stack is a close to open , pop 

                if stack and stack[-1] == closeToOpen[c] : 

                    stack.pop() 

                else : 

                    return False 

            else : 

                stack.append(c) 

        return True if not stack else False 
        