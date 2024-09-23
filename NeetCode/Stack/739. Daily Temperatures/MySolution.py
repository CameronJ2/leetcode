from typing import List

class BruteForce:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = []
        
        
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] - temperatures[i] > 0:
                    answer.append(j - i)
                    break
                elif j == len(temperatures) - 1:
                    answer.append(0)
                j += 1
        
        answer.append(0)
        return answer
    
class MyOptimal:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        tracker: List[int] = []
        popped: int = 0
        
        for i in range(len(temperatures)):
            if i == 0:
                tracker.append([i, temperatures[i]])
                continue
            
            j = 0
            
            while j < len(tracker):
                temp = tracker[j][0]
                iTemp = temperatures[i]
                jTemp = tracker[j][1]
                if temperatures[i] > tracker[j][1]:
                    answer[tracker[j][0]] = i - tracker[j][0]
                    tracker.pop(j)
                    continue
                j += 1
            
            tracker.append([i, temperatures[i]])
        
        return answer
                    
                
                
                
                    

bruteForce = BruteForce()

optimal = MyOptimal()

numbers = [30,60,90]

print(optimal.dailyTemperatures(numbers))
                    
        