from typing import List

class BruteForce:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into a list of tuples and sort by position
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        time_to_reach = 0

        for pos, spd in cars:
            # Calculate the time to reach the target
            time = (target - pos) / spd
            
            # If the current car takes longer than the last one processed, it forms a new fleet
            if time > time_to_reach:
                fleets += 1
                time_to_reach = time  # Update the time to the current car's time
        
        return fleets


mySolution = BruteForce()

# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]

# target = 10
# position = [3]
# speed = [3]

# target = 100
# position = [0,2,4]
# speed = [4,2,1]

# target = 13
# position = [10,2,5,7,4,6,11]
# speed = [7,5,10,5,9,4,1]

target = 17
position = [8,12,16,11,7]
speed = [6,9,10,9,7]



print(mySolution.carFleet(target, position, speed))