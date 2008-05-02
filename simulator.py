import car
import time
import road
import trafficLight

class Simulator:
   
    def __init__(self):
        self.light = trafficLight.TrafficLight(5)
        
        speeds = [(0, lambda: 2), (15, lambda: 4), (30, self.light.getSpeed),(31, lambda: 5),(50, lambda: 2), (80, lambda: 4)]
        self.theRoad = road.Road(speeds)
        nullCar = car.Car(1000000, 0, None, self.theRoad)
        a = car.Car(40, 0.5, nullCar, self.theRoad)
        b = car.Car(20, 1.3, a, self.theRoad)
        c = car.Car(10, 0.8, b, self.theRoad)
        d = car.Car(2, 0.65, c, self.theRoad)
        e = car.Car(1, 1.8, d, self.theRoad)
        self.carQueue = [a,b,c,d,e]
        
    def tick(self):
        self.light.tick()
        carsAndSpeeds = []
        cars = []
        speeds = []
        carsAndSpeeds.append(cars)
        carsAndSpeeds.append(speeds)
        
        firstCarPos=self.carQueue[0].getPosition()
        
        for currentCar in self.carQueue:
            currentCar.move()
            carPos = currentCar.getPosition()
            cars.append(carPos)            
        
        for i in range(0, firstCarPos+10):
            if self.theRoad.hasSpeedLimitChangeAt(i):
                speeds.append(i)
        
        return carsAndSpeeds
        
    def visualize(self):
        currpos = 0
        road = ""
        reverselist = list(self.carQueue)
        reverselist.reverse()
        for currentCar in reverselist:
            for i in range (currpos,currentCar.getPosition()):
                if self.theRoad.hasSpeedLimitChangeAt(i):
                    road += "|"
                else:
                    road += "."
            road+=currentCar.getRepresentation()
            currpos = currentCar.getPosition()+1
        print road   
        
            