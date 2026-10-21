class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #Stack solution for sure 

        stack = [] 

        for c in tokens : 

            #Evaluate the sign of the operation for sure 

            if c == "+" :

                stack.append(stack.pop() + stack.pop()) 

            elif c == "-" : 

                a, b = stack.pop(), stack.pop() 

                stack.append(b - a) 


            elif c == "*" : 

                stack.append(stack.pop() * stack.pop()) 

            elif c == "/" : 

                a, b = stack.pop(), stack.pop() 

                stack.append(int(float(b) / a))

            else : 

                stack.append(int(c))


        return stack[0]
        