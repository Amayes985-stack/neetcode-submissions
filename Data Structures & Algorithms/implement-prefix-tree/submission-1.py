
#Class treeNode 

class TrieNode : 

    def __init__(self):

        self.children = {}

        self.endOfWord = False 


class PrefixTree:

    def __init__(self):

        self.root = TrieNode() 
    

    def insert(self, word: str) -> None:

        #How to insert 

        current = self.root 

        #For every character in words 

        for c in word : 

            #Now if the current child is None existent, append it to the node 

            if c not in current.children : 

                current.children[c] = TrieNode()

            #Otherwise move to the next child 

            current = current.children[c] 

        #Mark the end of word 

        current.endOfWord = True 


    def search(self, word: str) -> bool:

        current = self.root #Keep track of the root 

        #Look for the position of i 

        for c in word : 

            #If the word I'm looking for is not there -> False 

            if c not in current.children : 

                return False 

            #Otherwise look for the rest 

            current = current.children[c] 

        #Check whether it's the end of the word 

        return current.endOfWord 
         

    def startsWith(self, prefix: str) -> bool:

        #Same thing but with children for sure 

        current = self.root 

        for c in prefix : 

            if c not in current.children : 

                return False 

            current = current.children[c] 

        return True 
        