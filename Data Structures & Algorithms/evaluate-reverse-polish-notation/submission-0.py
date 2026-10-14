class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 

        for character in tokens : 

            if character == "+" : 

                stack.append(stack.pop() + stack.pop()) 

            elif character == "*" : 

                stack.append(stack.pop() * stack.pop()) 

            elif character == "/" : 

                a,b = stack.pop(), stack.pop() 

                stack.append(int(float(b) / a)) 

            elif character == "-" : 
                
                a,b = stack.pop(), stack.pop() 
                stack.append(b-a) 

            else : 

                stack.append(int(character)) 

        return stack[0]



        