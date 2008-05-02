import unittest

class Road:
    
    # speedlimits: Tuple (startposition, speedlimit)
    #   must be sorted ascending on position, first position must always be 0
    def __init__(self, speedlimits):
        self.speedlimits = speedlimits
    
    def getSpeedLimit(self, position):
        lastSpeedFunction = self.speedlimits[0][1];
        for currentPos,speedlimit in self.speedlimits:
            if currentPos>position:
                return lastSpeedFunction()
            lastSpeedFunction = speedlimit
        return lastSpeedFunction()
    
    def hasSpeedLimitChangeAt(self, pos):
        for currentPos, speedLimit in self.speedlimits:
            if currentPos == pos:
                return True
        return False


if __name__ == "__main__":
    class Test(unittest.TestCase):

        def getRoad(self):
            return Road([(0,self.speed5),(5,self.speed7)])

        def testSpeedlimitAtPositionZero(self):
            road = self.getRoad() 
            self.assertEquals(5,road.getSpeedLimit(0))
        
        def testSpeedlimitAtPositionWithChangedSpeedlimit(self):
            road = self.getRoad() 
            self.assertEquals(7,road.getSpeedLimit(5))
        
        def testSpeedlimitAfterPositionWithChangedSpeedlimit(self):
            road = self.getRoad() 
            self.assertEquals(7,road.getSpeedLimit(6))
        
        def testSpeedlimitAfterAllTuples(self):
            road = self.getRoad() 
            self.assertEquals(7,road.getSpeedLimit(100))            
  
        def testOddNumberReturn(self):
            self.assertEquals
  
        def speed5(self):
            return 5
        
        def speed7(self):
            return 7
        
    
    unittest.main()