class TimeMap:

    def __init__(self):

        self.keyStore = {} 

    
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keyStore : 

            self.keyStore[key] = [] 

        self.keyStore[key].append([value, timestamp]) 


        

    def get(self, key: str, timestamp: int) -> str:

        res, values = "", self.keyStore.get(key, []) 

        head, tails = 0, len(values) - 1 

        while head <= tails : 

            middle = (head + tails) // 2 

            if values[middle][1] <= timestamp: 

                res = values[middle][0] 

                head = middle + 1 

            else : 

                tails = middle - 1 

        return res 
        
