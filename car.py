import random
import road
import unittest

class Car:
    
    lookaheadDistance = 5
    
    def __init__(self, pos, speedFactor, carinfront, theRoad):
        self.pos = pos
        self.speed = 0.0
        self.speedFactor = speedFactor
        self.carinfront = carinfront 
        self.theRoad = theRoad
        self.lastSpeed = -1.0
        self.speedChangeFactor = 0.9

    def getDesiredSpeed(self):
        return float(self.speedFactor * self.getSpeedLimit())

    def getSpeedLimit(self):
        for i in range(1, self.lookaheadDistance):
            if (self.theRoad.hasSpeedLimitChangeAt(self.pos + i)):
                if (self.theRoad.getSpeedLimit(self.pos + i)<self.theRoad.getSpeedLimit(self.pos)):
                    return (self.theRoad.getSpeedLimit(self.pos + i) + self.theRoad.getSpeedLimit(self.pos))/2
                else: 
                    return self.theRoad.getSpeedLimit(self.pos) 
        return self.theRoad.getSpeedLimit(self.pos)
    
    def __calculateSpeed(self):
        self.speed = self.getDesiredSpeed()
        carinfrontpos = self._getCarInFrontPosition()
        if carinfrontpos - self.pos <= self.lookaheadDistance:
            if self.speed > self.carinfront.speed:
                self.speed = self.speed*self.speedChangeFactor
            elif self.speed < self.carinfront.speed:
                self.speed = self.speed/self.speedChangeFactor
        self.lastSpeed = self.speed
    
    def _getCarInFrontPosition(self):
        return self.carinfront.pos
        
    def move(self):
        self.__calculateSpeed()
        self.pos = self.pos + int(self.speed)
        self.__avoidCrashing()

    def __avoidCrashing(self):
        if self.pos >= self._getCarInFrontPosition():
            self.pos = self._getCarInFrontPosition() - 1

    def getPosition(self):
        return self.pos % 80


if __name__ == "__main__":
    class Test(unittest.TestCase):

        def testReduceSpeedWhenCarInFrontHasZeroSpeed(self):
            speedlimit = 10
            thisCarPos = 1
            otherCarPos = 10
            car = Car(thisCarPos,1.0,self._getDummyCar(otherCarPos),self.__getDummyRoad(speedlimit))
            self.assertEquals(0, car.speed)
            car.move()
            self.assertEquals(speedlimit*car.speedFactor*car.speedChangeFactor, car.speed)
        
        def testReduceSpeedWhenCarInFrontMovesSlowerInsideLookahead(self):
            speedlimit = 10
            myRoad = road.Road([(0,lambda: speedlimit)])
            dummyCar = self._getDummyCar(1000)
            firstCar = Car(5,0.8,dummyCar,myRoad)
            car = Car(1,1.0,firstCar,myRoad)
            firstCar.move()
            car.move()
            self.assertEquals(speedlimit*car.speedChangeFactor,car.speed)
        
        def testDriveDesiredSpeedWhenCarInFrontIsOutsideLookahead(self):
            speedlimit = 10
            car = Car(1,1.2,self._getDummyCar(1000),road.Road([(0,lambda: speedlimit)]))
            car.move()
            self.assertEquals(car.getDesiredSpeed(),car.speed)
            self.assertEquals(12,car.speed)
            self.assertEquals(13,car.pos)
        
        def testCalculatesCorrectSpeedLimit(self):
            initLimit = 3
            firstLimit = 4
            secondLimit = 6
            thirdLimit = 5
            car = Car(1, 1.0, self._getDummyCar(1000), road.Road([
                                                                  (0, lambda: initLimit), 
                                                                  (3, lambda: firstLimit), 
                                                                  (5, lambda: secondLimit), 
                                                                  (7, lambda: thirdLimit)]))
            car.lookaheadDistance = 7
            
            self.assertEquals(initLimit, car.getSpeedLimit())
            
            car.pos = 3
            self.assertEquals(firstLimit, car.getSpeedLimit())
            
            car.pos = 4
            self.assertEquals(firstLimit, car.getSpeedLimit())
            
            car.pos = 5
            self.assertEquals((thirdLimit+secondLimit)/2, car.getSpeedLimit())
            
            car.pos = 7
            self.assertEquals(thirdLimit, car.getSpeedLimit())
            
            car.pos = 80
            self.assertEquals(thirdLimit, car.getSpeedLimit())
        
        def _getDummyCar(self,position):
            return Car(position,1.0,None,None)
        
        def __getDummyRoad(self, speedLimit):
            return road.Road([(0,lambda: speedLimit)])
    
    unittest.main()
