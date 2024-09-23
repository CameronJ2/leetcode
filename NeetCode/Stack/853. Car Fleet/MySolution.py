from typing import List


class BruteForce:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        convoys = 0
        cars: List[List[int]] = []
        
        if len(position) == 1:
            return 1
        
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        
        cars.sort(reverse=True,key=lambda x: x[0])
        
        while len(cars) != 0:
            for i in range(len(cars)):
                cars[i][0] += cars[i][1]
        
            idx = 0
            
            while idx < len(cars):
                while not idx == len(cars) - 1 and cars[idx][0] <= cars[idx+1][0]:
                    cars.pop(idx+1)
                
                if cars[idx][0] >= target:
                    
                    # while not idx == len(cars) - 1 and cars[idx + 1][0] > target:
                    #     cars.pop(idx+1)
                    
                    convoys += 1
                    cars.pop(idx)
                
                idx += 1
        return convoys
        
        # cars.sort(key=lambda x: x[0])
        
        # while len(cars) != 0:
        #     for i in range(len(cars)):
        #         cars[i][0] += cars[i][1]
                
        #     idx = 0
            
        #     while idx < len(cars):
                
                
        #         while not idx == len(cars) - 1 and cars[idx][0] >= cars[idx+1][0]:
        #             # convoys += 1
        #             cars.pop(idx)
        #             continue
        #         if cars[idx][0] >= target:
        #             convoys += 1
        #             cars.pop(idx)
        #         idx += 1
        # return convoys
                
        
        
        
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