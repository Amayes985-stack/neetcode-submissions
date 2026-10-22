class TimeMap:

    def __init__(self):

        self.keystore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keystore : 

            self.keystore[key] = [] 

        self.keystore[key].append([value, timestamp])
        


    def get(self, key: str, timestamp: int) -> str:

        result, values = "", self.keystore.get(key, []) 

        top, bottom = 0, len(values) - 1 

        while top <= bottom : 

            mid = (top + bottom) // 2 

            if values[mid][1] <= timestamp : 

                result = values[mid][0] 

                top = mid + 1 

            else : 

                bottom = mid - 1 

        return result 
        
