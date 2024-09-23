from typing import List

class Optimal:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        tracker = []

        for i in range(len(temperatures)):
            # Check if current temperature is warmer than the temperatures in tracker
            while tracker and temperatures[i] > temperatures[tracker[-1]]:
                idx = tracker.pop()
                answer[idx] = i - idx
            
            # Add the current index to the tracker
            tracker.append(i)
        
        return answer
                    
                
                
                
                    

bruteForce = Optimal()

optimal = Optimal()

numbers = [30,60,90]

print(optimal.dailyTemperatures(numbers))