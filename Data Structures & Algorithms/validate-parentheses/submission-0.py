class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] 

        Map = { ")" : "(" , "]" : "[" , "}" : "{" } 

        for character in s : 

            if character in Map : 

                if stack and stack[-1] == Map[character] : 

                    stack.pop() 

                else : 

                    return False 

            else : 

                stack.append(character) 

        return True if not stack else False 

    # O(n) , O(n)
        