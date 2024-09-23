class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length: int = min(len(a), len(b))
        smaller: str
        a = a[::-1]
        b = b[::-1]
        result: str = ""
        sum: int
        idx: int
        
        if len(a) < len(b):
            smaller = a
            larger = b
        else:
            smaller = b
            larger = a
        
        smallerList: list[str] = []
        largerList: list[str] = []
        
        for char in smaller:
            smallerList.append(char)
        for char in larger:
            largerList.append(char)
            
        for i in range(len(smallerList)):
            sum = int(largerList[i]) + int(smaller[i])
            if sum == 0:
                result += "0"
            elif sum == 1:
                result += "1"
            elif sum == 2:
                result += "0"
                if (i == len(largerList) - 1):
                    largerList.append("1")
                else:
                    largerList[i+1] = str(int(largerList[i+1]) + 1)
            elif sum == 3:
                result += "1"
                if (i == len(largerList) - 1):
                    largerList.append("1")
                else:
                    largerList[i+1] = str(int(largerList[i+1]) + 1)
        
        idx = len(smallerList)
        
        while idx < len(largerList):
            if largerList[idx] == "0":
                result += "0"
            if largerList[idx] == "1":
                result += "1"
            if largerList[idx] == "2":
                result += "0"
                if (idx == len(largerList) - 1):
                    result += "1"
                else:
                    largerList[idx+1] = str(int(largerList[idx+1]) + 1)
            idx += 1
            
        
        return result[::-1]
            
        
mySol = Solution()

a = "1111"
b = "1111"

print(mySol.addBinary(a, b))